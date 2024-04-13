from typing import Annotated, Union
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import BaseModel
from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime, timedelta, timezone
from .database import SessionLocal, engine
import bcrypt

models.Base.metadata.create_all(bind=engine)

# To get a string like this in Windows run:
# .\generate_random_hex.ps1
# Look for this file in the project main directory.
SECRET_KEY = "54ad26c59098ffb982dbd2a9b5b520b4"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Union[str, None] = None

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# Hash a password using bcrypt.
def hash_password(password):
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    return hash_password

# Check if the provided password matches the stored password (hashed)
def verify_password(plain_password, hashed_password):
    password_byte_enc = plain_password.encode('utf-8')
    return bcrypt.checkpw(password = password_byte_enc, hashed_password = hashed_password)

def authenticate_user(db: Session, username: str, password: str) -> Union[models.User, bool]:
    user = get_user_by_username(db, username)
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
    db = next(get_db())
    user = get_user_by_username(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(
        current_user: Annotated[models.User, Depends(get_current_user)]):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def create_user(db: Session, user: schemas.UserCreate):
    new_hashed_password = hash_password(user.hashed_password)
    db_user = models.User(
        username=user.username, 
        hashed_password=new_hashed_password, 
        user_first_name=user.user_first_name,
        user_middle_initial=user.user_middle_initial,
        user_last_name=user.user_last_name,
        user_date_of_birth=user.user_date_of_birth,
        email=user.email,
        user_date_created=datetime.now(),
        facility_id=user.facility_id,
        is_active=True,
        user_street_address=user.user_street_address,
        user_city=user.user_city,
        user_state=user.user_state,
        user_country=user.user_country,
        user_phone_number=user.user_phone_number)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_activity_logs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.UserActivityLog).offset(skip).limit(limit).all()

def create_user_activity_log(db: Session, ualog: schemas.UserActivityLogCreate, user_id: int):
    db_user_activity_log = models.UserActivityLog(**ualog.model_dump(), user_id=user_id)
    db.add(db_user_activity_log)
    db.commit()
    db.refresh(db_user_activity_log)
    return db_user_activity_log