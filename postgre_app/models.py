from sqlalchemy import Column, Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import date, datetime
from database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True, nullable=False)
    user_first_name = Column(String, nullable=False)
    user_middle_initial = Column(String)
    user_last_name = Column(String, nullable=False)
    user_date_of_birth = Column(date, nullable=False)
    user_email = Column(String, unique=True)
    user_date_created = Column(datetime, nullable=False)
    facility_id = Column(String, nullable=False)
    user_enabled = Column(Boolean, nullable=False)
    user_hashed_password = Column(String, nullable=False)
    user_street_address = Column(String)
    user_city = Column(String)
    user_state = Column(String)
    user_country = Column(String)
    user_phone_number = Column(String)

    patient = relationship("Patient", back_populates="user")
    physician_assigned_patient = relationship("PhysicianAssignedPatient", back_populates="user")
    user_authorized_facility = relationship("UserAuthorizedFacility", back_populates="user")

class Patient(Base):
    __tablename__ = "patients"

    patient_user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    patient_provider = Column(String, nullable=False)
    patient_provider_id = Column(String, nullable=False)
    patient_room = Column(String)
    patient_current_gender = Column(String, nullable=False)
    patient_type = Column(String, nullable=False)
    patient_language_preference = Column(String)
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
    patient_race = relationship("PatientRace", back_populates="patient")

class PhysicianAssignedPatient(Base):
    __tablename__ = "physician_assigned_patients"

    staff_user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    patient_user_id = Column(Integer, nullable=False)

    user = relationship("User", back_populates="physician_assigned_patient")

class UserAuthorizedFacility(Base):
    __tablename__ = "user_authorized_facilities"

    user_authorized_facilities_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    facility_id = Column(String, nullable=False)

    user = relationship("User", back_populates="user_authorized_facility")

class PatientRace(Base):
    __tablename__ = "patient_races"

    patient_race_id = Column(Integer, primary_key=True)
    patient_user_id = Column(Integer, ForeignKey("patients.patient_user_id"), nullable=False)
    patient_race = Column(String, nullable=False)

    patient = relationship("Patient", back_populates="patient_race")