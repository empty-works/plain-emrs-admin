from typing import Annotated
from datetime import timedelta
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from postgre_app import crud, models, schemas

app = FastAPI()

@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
    ) -> crud.Token:
    db = next(crud.get_db())
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=crud.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = crud.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return crud.Token(access_token=access_token, token_type="bearer")

@app.get("/users/me")
async def read_users_me(current_user: Annotated[models.User, Depends(crud.get_current_user)]):
    return current_user

@app.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(crud.get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(crud.get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(crud.get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/users/{user_id}/user_activity_logs", response_model=schemas.UserActivityLog)
def create_activity_log_for_user(
    user_id: int, user_activity_log: schemas.UserActivityLogCreate, db: Session = Depends(crud.get_db)
):
    return crud.create_user_activity_log(db=db, user_activity_log=user_activity_log, user_id=user_id)

@app.get("/user_activity_logs/", response_model=list[schemas.UserActivityLog])
def read_user_activity_logs(skip: int = 0, limit: int = 100, db: Session = Depends(crud.get_db)):
    user_activity_logs = crud.get_user_activity_logs(db, skip=skip, limit=limit)
    return user_activity_logs