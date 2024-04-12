from sqlalchemy.orm import Session
from passlib.context import CryptContext
from . import models, schemas
import datetime

# To get a string like this in Windows run:
# .\generate_random_hex.ps1
# Look for this file in the project main directory.
SECRET_KEY = "54ad26c59098ffb982dbd2a9b5b520b4"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_password_hash(password):
    return pwd_context.hash(password)

def create_user(db: Session, user: schemas.UserCreate):
    new_hashed_password = get_password_hash(user.hashed_password)
    db_user = models.User(
        username=user.username, 
        hashed_password=new_hashed_password, 
        user_first_name=user.user_first_name,
        user_middle_initial=user.user_middle_initial,
        user_last_name=user.user_last_name,
        user_date_of_birth=user.user_date_of_birth,
        email=user.email,
        user_date_created=datetime.datetime.now(),
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