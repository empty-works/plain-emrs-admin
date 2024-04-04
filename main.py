from typing import Annotated, Union
from datetime import date, datetime, timedelta, timezone
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy.orm import Session

from postgre_app import crud, models, schemas
from postgre_app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

# To get a string like this in Windows run:
# .\generate_random_hex.ps1
# Look for this file in the project main directory.
SECRET_KEY = "54ad26c59098ffb982dbd2a9b5b520b4"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

hash_pwd1 = get_password_hash("fakehashedsecret1")
hash_pwd2 = get_password_hash("fakehashedsecret2")

fake_users_db = {
    "fakeuser1": {
        "username": "fakeuser1",
        "first_name": "Fake",
        "middle_initial": "A",
        "last_name": "User1",
        "date_of_birth": date(1996, 12, 11),
        "date_created": datetime.now(),
        "email": "fakeuser1@example.com",
        "facility_id": "The Facility",
        "hashed_password": hash_pwd1,
        "enabled": True
    },
    "fakeuser2": {
        "username": "fakeuser2",
        "first_name": "Fake",
        "middle_initial": "E",
        "last_name": "User2",
        "date_of_birth": date(1995, 11, 11),
        "date_created": datetime.now(),
        "email": "fakeuser2@example.com",
        "facility_id": "The Facility",
        "hashed_password": hash_pwd2,
        "enabled": True
    },
}

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Union[str, None] = None

class User(BaseModel):
    username: str
    first_name: str
    middle_initial: Union[str, None] = None
    last_name: str
    date_of_birth: date
    date_created: datetime
    email: Union[str, None] = None
    facility_id: str
    enabled: bool

class UserInDB(User):
    hashed_password: str

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(
        current_user: Annotated[User, Depends(get_current_user)]):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
    ) -> Token:
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@app.get("/users/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user
