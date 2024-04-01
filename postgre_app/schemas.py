from typing import Union
from pydantic import BaseModel
from datetime import date, datetime

class AdmissionBase(BaseModel):
    date_of_admission: datetime
    admissions_description: str

class AdmissionCreate(AdmissionBase):
    medical_record_id: int

class Admission(AdmissionBase):
    admission_id: int
    medical_record_id: int



class ChiefComplaintBase(BaseModel):
    chief_complaint_statement: str
    chief_complaint_date: datetime

class ChiefComplaintCreate(ChiefComplaintBase):
    medical_record_id: int

class ChiefComplaint(ChiefComplaintBase): 
    chief_complaint_id: int
    medical_record_id: int
    medications: list[Medication] = []
    surgical_related_problems: list[SurgicalRelatedProblem] = []
    vitals: list[Vital] = []
    treatments: list[Treatment] = []
    review_of_systems: list[ReviewOfSystems] = []
    physical_exams: list[PhysicalExam] = []
    assessments: list[Assessment] = []
    plans: list[Plan] = []
    histories_present_illness: list[HistoryPresentIllness] = []
    diagnoses: list[Diagnosis] = []
    medical_record_id: int

class MedicalRecordBase(BaseModel):
    patient_condition: str
    blood_transfusion_status: str

class MedicalRecordCreate(MedicalRecordBase):
    user_id: int

class MedicalRecord(MedicalRecordBase):
    medical_record_id: int
    user_id: int
    medical_record_created: datetime
    is_active: bool

    nurse_notes: list[NurseNote] = []
    social_history: SocialHistory
    appointments: list[Appointment] = []
    family_illnesses: list[FamilyIllness] = []
    medications: list[Medication] = []
    blood_relatives: list[BloodRelative] = []
    visits: list[Visit] = []
    allergies: list[Allergy] = []
    immunizations: list[Immunization] = []
    surgical_related_problems: list[SurgicalRelatedProblem] = []
    admissions: list[Admission] = []
    vitals: list[Vital] = []
    treatments: list[Treatment] = []
    reviews_of_systems: list[ReviewOfSystems] = []
    physical_exams: list[PhysicalExam] = []
    assessments: list[Assessment] = []
    plans: list[Plan] = []
    histories_present_illness: list[HistoryPresentIllness] = []
    diagnoses: list[Diagnosis] = []
    chief_complaints: list[ChiefComplaint] = []

class PatientBase(BaseModel):
    patient_provider: str
    patient_provider_id: str
    patient_room: Union[str, None] = None
    patient_current_gender: str
    patient_type: str
    patient_language_preference: Union[str, None] = None
    patient_street_address: Union[str, None] = None
    patient_city: Union[str, None] = None
    patient_state: Union[str, None] = None
    patient_country: Union[str, None] = None
    patient_phone_number: Union[str, None] = None
    patient_gender_at_birth: str
    patient_sexual_orientation: str
    patient_marital_status: str
    patient_living_arrangement: str
    patient_is_adopted: str
    patient_license_number: Union[str, None] = None
    patient_vehicle_serial_number: Union[str, None] = None
    patient_vehicle_plate_number: Union[str, None] = None
    patient_url: Union[str, None] = None
    patient_device_serial_number: Union[str, None] = None
    patient_ip_address: Union[str, None] = None

class PatientCreate(PatientBase):
    user_id: int

class Patient(PatientBase):
    user_id: int
    patient_race: str
    emergency_contacts: list[EmergencyContact] = []

class UserBase(BaseModel):
    username: str
    user_first_name: str
    user_middle_initial: Union[str, None] = None
    user_last_name: str
    user_date_of_birth: date
    email: Union[str, None] = None
    facility_id: str
    user_street_address: Union[str, None] = None
    user_city: Union[str, None] = None
    user_country: Union[str, None] = None
    user_phone_number: Union[str, None] = None

class UserCreate(UserBase):
    hashed_password: str

class User(UserBase):
    user_id: int
    user_date_created: datetime
    is_active: bool

    patient: Patient
    physician_assigned_patients: list[PhysicianAssignedPatient] = []
    user_authorized_facilities: list[UserAuthorizedFacility] = []
    user_login_logs: list[UserLoginLog] = []
    user_activity_logs: list[UserActivityLog] = []
    nonpatient: Nonpatient
    medical_record: MedicalRecord

    class Config:
        orm_mode = True