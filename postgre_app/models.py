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

    patient = relationship("Patient", back_populates="user")

class Patient(Base):
    __tablename__ = "patients"

    user_id = Column(Integer, ForeignKey("users.user_id"))
    patient_provider = Column(String, nullable=False)
    patient_provider_id = Column(String, nullable=False)
    patient_room = Column(String)
    patient_current_gender = Column(String, nullable=False)
    patient_type = Column(String, nullable=False)
    patient_language_preference = Column(String)
    patient_street_address = Column(String)
    patient_city = Column(String)
    patient_state = Column(String)
    patient_country = Column(String)
    patient_phone_number = Column(String)
    patient_gender_at_birth = Column(String, nullable=False)
    patient_sexual_orientation = Column(String, nullable=False)
    patient_marital_status = Column(String, nullable=False)
    patient_living_arrangement = Column(String, nullable=False)
    patient_is_adopted = Column(Boolean, nullable=False)
    patient_license_number = Column(String)
    patient_vehicle_serial_number = Column(String)
    patient_vehicle_plate_number = Column(String)
    patient_url = Column(String)
    patient_device_serial_number = Column(String)
    patient_ip_address = Column(String)

    user = relationship("User", back_populates="patient")