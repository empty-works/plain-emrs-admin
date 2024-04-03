from sqlalchemy.orm import Session
from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def get_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.hashed_password + "notreallyhashed"
    db_user = models.User(username=user.username, hashed_password=fake_hashed_password)
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