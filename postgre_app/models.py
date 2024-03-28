from sqlalchemy import Column, Boolean, ForeignKey, Integer, BigInteger, String
from sqlalchemy.orm import relationship
from datetime import date, datetime
from database import Base

class EmergencyContact(Base):
    __tablename__ = "emergency_contacts"

    emergency_contact_id = Column(BigInteger, primary_key=True, nullable=False)
    user_id = Column(BigInteger, ForeignKey("patients.user_id"), nullable=False)
    emergency_contact_given_name = Column(String(50), nullable=False)
    emergency_contact_middle_initial = Column(String(1))
    emergency_contact_last_name = Column(String(50), nullable=False)
    emergency_contact_phone_number = Column(String(15), nullable=False)
    emergency_contact_email = Column(String(254))

    patient = relationship("Patient", back_populates="emergency_contact")

class MedicalRecord(Base):
    __tablename__ = "medical_records"

    medical_record_id = Column(BigInteger, primary_key=True, nullable=False)
    user_id = Column(BigInteger, ForeignKey("users.user_id"), nullable=False)
    patient_condition = Column(String, nullable=False)
    medical_record_created = Column(datetime, nullable=False)
    is_active = Column(Boolean, nullable=False)
    blood_transfusion_status = Column(String, nullable=False)

    user = relationship("User", back_populates="medical_record")
    nurse_note = relationship("NurseNote", back_populates="medical_record")
    social_history = relationship("SocialHistory", back_populates="medical_record")

class Nonpatient(Base):
    __tablename__ = "nonpatients"

    user_id = Column(BigInteger, ForeignKey("users.user_id"), nullable=False)
    nonpatient_organization = Column(String(100), nullable=False)
    nonpatient_description = Column(String)
    nonpatient_ward_id = Column(String(75))
    nonpatient_staff_position_id = Column(String(75))
    nonpatient_specialty_id = Column(String(75))

    user = relationship("User", back_populates="nonpatient")

class NurseNote(Base):
    __tablename__ = "nurse_notes"

    nurse_note_id = Column(BigInteger, primary_key=True, nullable=False)
    medical_record_id = Column(BigInteger, ForeignKey("medical_records.medical_record_id"), nullable=False)
    nurse_note_date_posted = Column(datetime, nullable=False)
    nurse_note_focus = Column(String, nullable=False)
    nurse_note_text = Column(String, nullable=False)

    medical_record = relationship("MedicalRecord", back_populates="nurse_note")

class Patient(Base):
    __tablename__ = "patients"

    user_id = Column(BigInteger, ForeignKey("users.user_id"), nullable=False)
    patient_provider = Column(String(100), nullable=False)
    patient_provider_id = Column(String(60), nullable=False)
    patient_room = Column(String(10))
    patient_current_gender = Column(String(80), nullable=False)
    patient_type = Column(String(20), nullable=False)
    patient_language_preference = Column(String(45))
    patient_gender_at_birth = Column(String(5), nullable=False)
    patient_sexual_orientation = Column(String(75), nullable=False)
    patient_marital_status = Column(String(45), nullable=False)
    patient_living_arrangement = Column(String(75), nullable=False)
    patient_is_adopted = Column(Boolean, nullable=False)
    patient_license_number = Column(String(45))
    patient_vehicle_serial_number = Column(String(45))
    patient_vehicle_plate_number = Column(String(45))
    patient_url = Column(String(45))
    patient_device_serial_number = Column(String(45))
    patient_ip_address = Column(String(45))

    user = relationship("User", back_populates="patient")
    patient_race = relationship("PatientRace", back_populates="patient")
    emergency_contact = relationship("EmergencyContact", back_populates="emergency_contact")

class PatientRace(Base):
    __tablename__ = "patient_races"

    patient_race_id = Column(BigInteger, primary_key=True, nullable=False)
    user_id = Column(BigInteger, ForeignKey("patients.user_id"), nullable=False)
    patient_race = Column(String(254), nullable=False)

    patient = relationship("Patient", back_populates="patient_race")

class PhysicianAssignedPatient(Base):
    __tablename__ = "physician_assigned_patients"

    staff_user_id = Column(BigInteger, ForeignKey("users.user_id"), nullable=False)
    patient_user_id = Column(BigInteger, nullable=False)

    user = relationship("User", back_populates="physician_assigned_patient")

class SocialHistory(Base):
    __tablename__ = "social_histories"

    social_history_id = Column(BigInteger, primary_key=True, nullable=False)
    medical_record_id = Column(BigInteger, ForeignKey("medical_records.medical_record_id"))
    substances = Column(String)
    occupation = Column(String)
    sexual_behavior = Column(String)
    prison = Column(String)
    travel = Column(String)
    exercise = Column(String)
    diet = Column(String)
    firearms_in_household = Column(String)

    medical_record = relationship("MedicalRecord", back_populates="social_history")

class User(Base):
    __tablename__ = "users"

    user_id = Column(BigInteger, primary_key=True, nullable=False)
    username = Column(String(75), unique=True, index=True, nullable=False)
    user_first_name = Column(String(35), nullable=False)
    user_middle_initial = Column(String(1))
    user_last_name = Column(String(50), nullable=False)
    user_date_of_birth = Column(date, nullable=False)
    user_email = Column(String(254), unique=True)
    user_date_created = Column(datetime, nullable=False)
    facility_id = Column(String(75), nullable=False)
    user_enabled = Column(Boolean, nullable=False)
    user_hashed_password = Column(String(68), nullable=False)
    user_street_address = Column(String(100))
    user_city = Column(String(45))
    user_state = Column(String(50))
    user_country = Column(String(55))
    user_phone_number = Column(String(15))

    patient = relationship("Patient", back_populates="user")
    physician_assigned_patient = relationship("PhysicianAssignedPatient", back_populates="user")
    user_authorized_facility = relationship("UserAuthorizedFacility", back_populates="user")
    user_login_log = relationship("UserLoginLog", back_populates="user")
    user_activity_log = relationship("UserActivityLog", back_populates="user")
    nonpatient = relationship("Nonpatient", back_populates="user")
    medical_record = relationship("MedicalRecord", back_populates="user")

class UserActivityLog(Base):
    __tablename__ = "user_activity_logs"

    user_activity_log_id = Column(BigInteger, primary_key=True, nullable=False)
    user_id = Column(BigInteger, nullable=False)
    user_date_time_of_activity = Column(datetime, nullable=False)
    activity_description = Column(String, nullable=False)

    user = relationship("User", back_populates="user_activity_log")

class UserAuthorizedFacility(Base):
    __tablename__ = "user_authorized_facilities"

    user_authorized_facility_id = Column(BigInteger, primary_key=True, nullable=False)
    user_id = Column(BigInteger, ForeignKey("users.user_id"), nullable=False)
    facility_id = Column(String(75), nullable=False)

    user = relationship("User", back_populates="user_authorized_facility")

class UserLoginLog(Base):
    __tablename__ = "user_login_logs"

    user_login_log_id = Column(BigInteger, primary_key=True, nullable=False)
    user_id = Column(BigInteger, ForeignKey("users.user_id"), nullable=False)
    user_date_time_of_activity = Column(datetime, nullable=False) 
    activity_description = Column(String, nullable=False)

    user = relationship("User", back_populates="user_login_log")