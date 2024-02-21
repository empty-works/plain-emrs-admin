from sqlalchemy import Column, Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import date, datetime
from database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String, nullable=False)
    middle_initial = Column(String)
    last_name = Column(String, nullable=False)
    date_of_birth = Column(date, nullable=False)
    email = Column(String)
    date_created = Column(datetime, nullable=False)
    facility_id = Column(String, nullable=False)
    enabled = Column(Boolean, nullable=False)
    hashed_password = Column(String, nullable=False)