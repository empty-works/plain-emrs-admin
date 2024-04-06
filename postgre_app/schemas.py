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

class AllergyBase(BaseModel):
    allergy_name: str
    allergy_severity: Union[str, None] = None
    additional_information: Union[str, None] = None

class AllergyCreate(AllergyBase):
    medical_record_id: int

class Allergy(AllergyBase):
    allergy_id: int
    medical_record_id: int

class AppointmentBase(BaseModel):
    appointment_title: str
    appointment_date: datetime
    appointment_description: str

class AppointmentCreate(AppointmentBase):
    medical_record_id: int

class Appointment(AppointmentBase):
    appointment_id: int
    medical_record_id: int

class AssessmentBase(BaseModel):
    assessments_summation: str

class AssessmentCreate(AssessmentBase):
    chief_complaint_id: int
    medical_record_id: int

class Assessment(AssessmentBase):
    assessment_id: int
    chief_complaint_id: int
    medical_record_id: int

class BloodRelativeBase(BaseModel):
    mother_status: str
    father_status: str
    mother_deceased_age: Union[int, None] = None
    father_deceased_age: Union[int, None] = None
    num_sisters_alive: int
    num_brothers_alive: int
    num_daughters_alive: int
    num_sons_alive: int
    mother_cause_of_death: Union[str, None] = None
    father_cause_of_death: Union[str, None] = None

class BloodRelativeCreate(BloodRelativeBase):
    medical_record_id: int

class BloodRelative(BloodRelativeBase):
    blood_relatives_id: int
    medical_record_id: int

class DiagnosisBase(BaseModel):
    diagnosis_title: str
    diagnosis_date: datetime
    diagnosis_description: str

class DiagnosisCreate(DiagnosisBase):
    chief_complaint_id: int
    medical_record_id: int

class Diagnosis(DiagnosisBase):
    diagnosis_id: int
    chief_complaint_id: int
    medical_record_id: int

class EmergencyContactBase(BaseModel):
    emergency_contact_given_name: str
    emergency_contact_middle_initial: Union[str, None] = None
    emergency_contact_last_name: str
    emergency_contact_phone_number: str
    emergency_contact_email: Union[str, None] = None

class EmergencyContactCreate(EmergencyContactBase):
    user_id: int

class EmergencyContact(EmergencyContactBase):
    emergency_contact_id: int
    user_id: int

class FamilyIllnessBase(BaseModel):
    illness: str
    father: Union[bool, None] = None
    mother: Union[bool, None] = None
    brothers: Union[bool, None] = None
    sisters: Union[bool, None] = None
    sons: Union[bool, None] = None
    daughters: Union[bool, None] = None
    grandparents: Union[bool, None] = None

class FamilyIllnessCreate(FamilyIllnessBase):
    medical_record_id: int

class FamilyIllness(FamilyIllnessBase):
    family_illness_id: int
    medical_record_id: int

class HistoryPresentIllnessBase(BaseModel):
    hpi_location: Union[str, None] = None
    hpi_character: Union[str, None] = None
    hpi_duration: Union[str, None] = None
    hpi_onset: Union[str, None] = None
    hpi_modifying_factors: Union[str, None] = None
    hpi_radiation: Union[str, None] = None
    hpi_temporal_pattern: Union[str, None] = None
    hpi_severity: Union[str, None] = None
    hpi_description: Union[str, None] = None

class HistoryPresentIllnessCreate(HistoryPresentIllnessBase):
    chief_complaint_id: int
    medical_record_id: int

class HistoryPresentIllness(HistoryPresentIllnessBase):
    history_present_illness_id: int
    chief_complaint_id: int
    medical_record_id: int

class IllnessBase(BaseModel):
    illnesses_diagnosis_date: Union[datetime, None] = None
    illnesses_diagnosis_id: Union[int, None] = None
    illnesses_treatment_id: Union[int, None] = None
    illnesses_medication_id: Union[int, None] = None
    illnesses_surgical_related_problem_id: Union[int, None] = None
    illnesses_allergy_id: Union[int, None] = None

class IllnessCreate(IllnessBase):
    chief_complaint_id: int
    medical_record_id: int

class Illness(IllnessBase):
    illness_id: int
    chief_complaint_id: int
    medical_record_id: int

class ImmunizationBase(BaseModel):
    immunization: str

class ImmunizationCreate(ImmunizationBase):
    medical_record_id: int

class Immunization(ImmunizationBase):
    immunization_id: int
    medical_record_id: int

class MedicationBase(BaseModel):
    medication_name: str
    medication_is_current: bool
    medication_description: Union[str, None] = None
    medication_frequency: Union[str, None] = None
    medication_dosage: Union[float, None] = None
    medication_start_date: Union[datetime, None] = None
    medication_end_date: Union[datetime, None] = None
    medication_healthcare_provider: Union[str, None] = None

class MedicationCreate(MedicationBase):
    chief_complaint_id: int
    medical_record_id: int

class Medication(MedicationBase):
    medication_id: int
    chief_complaint_id: int
    medical_record_id: int
    
class NonpatientBase(BaseModel):
    nonpatient_organization: str
    nonpatient_description: Union[str, None] = None
    nonpatient_ward_id: Union[str, None] = None
    nonpatient_staff_position_id: Union[str, None] = None
    nonpatient_specialty_id: Union[str, None] = None

class NonpatientCreate(NonpatientBase):
    user_id: int

class Nonpatient(NonpatientBase):
    user_id: int

class NurseNoteBase(BaseModel):
    nurse_note_date_posted: datetime
    nurse_note_focus: str
    nurse_note_text: str

class NurseNoteCreate(NurseNoteBase):
    medical_record_id: int

class NurseNote(NurseNoteBase):
    nurse_note_id: int
    medical_record_id: int

class PatientRaceBase(BaseModel):
    patient_race: str

class PatientRaceCreate(PatientRaceBase):
    user_id: int

class PatientRace(PatientRaceBase):
    patient_race_id: int
    user_id: int

class PhysicalExamBase(BaseModel):
    physical_exam_heent: Union[str, None] = None
    physical_exam_respiratory: Union[str, None] = None
    physical_exam_cardiovascular: Union[str, None] = None
    physical_exam_abdominal: Union[str, None] = None
    physical_exam_limbs: Union[str, None] = None
    physical_exam_neurological: Union[str, None] = None
    physical_exam_date: datetime

class PhysicalExamCreate(PhysicalExamBase):
    chief_complaint_id: int
    medical_record_id: int

class PhysicalExam(PhysicalExamBase):
    physical_exam_id: int
    chief_complaint_id: int
    medical_record_id: int

class PhysicianAssignedPatientBase(BaseModel):
    patient_user_id: int

class PhysicianAssignedPatientCreate(PhysicianAssignedPatientBase):
    staff_user_id: int

class PhysicianAssignedPatient(PhysicianAssignedPatientBase):
    staff_user_id: int

class PlanBase(BaseModel):
    plans_summation: Union[str, None] = None

class PlanCreate(PlanBase):
    chief_complaint_id: int
    medical_record_id: int

class Plan(PlanBase):
    plan_id: int
    chief_complaint_id: int
    medical_record_id: int

class ReviewOfSystemsBase(BaseModel):
    review_of_systems_constitutional_symptoms: Union[str, None] = None
    review_of_systems_eyes: Union[str, None] = None
    review_of_systems_ears_nose_throat: Union[str, None] = None
    review_of_systems_cardiovascular: Union[str, None] = None
    review_of_systems_respiratory: Union[str, None] = None
    review_of_systems_gastrointestinal: Union[str, None] = None
    review_of_systems_genitournary: Union[str, None] = None
    review_of_systems_musculoskeletal: Union[str, None] = None
    review_of_systems_integumentary: Union[str, None] = None
    review_of_systems_neurological: Union[str, None] = None
    review_of_systems_psychiatric: Union[str, None] = None
    review_of_systems_endocrine: Union[str, None] = None
    review_of_systems_hematologic_lymphatic: Union[str, None] = None
    review_of_systems_allergic_immunologic: Union[str, None] = None
    review_of_systems_date: Union[datetime, None] = None

class ReviewOfSystemsCreate(ReviewOfSystemsBase):
    chief_complaints_id: int
    medical_record_id: int

class ReviewOfSystems(ReviewOfSystemsBase):
    review_of_systems_id: int
    chief_complaints_id: int
    medical_record_id: int

class SocialHistoryBase(BaseModel):
    substances: Union[str, None] = None
    occupation: Union[str, None] = None
    sexual_behavior: Union[str, None] = None
    prison: Union[str, None] = None
    travel: Union[str, None] = None
    exercise: Union[str, None] = None
    diet: Union[str, None] = None
    firearms_in_household: Union[str, None] = None

class SocialHistoryCreate(SocialHistoryBase):
    medical_record_id: int

class SocialHistory(SocialHistoryBase):
    social_history_id: int
    medical_record_id: int

class SurgicalRelatedProblemBase(BaseModel):
    surgical_related_problem: str
    surgical_related_problem_area: str
    surgical_related_problem_procedure: Union[str, None] = None
    surgical_related_problem_procedure_year: Union[date, None] = None

class SurgicalRelatedProblemCreate(SurgicalRelatedProblemBase):
    chief_complaint_id: int
    medical_record_id: int

class SurgicalRelatedProblem(SurgicalRelatedProblemBase):
    surgical_related_problem_id: int
    chief_complaint_id: int
    medical_record_id: int

class TreatmentBase(BaseModel):
    treatment_healthcare_provider: Union[str, None] = None
    treatment_type: str
    treatment_description: Union[str, None] = None
    treatment_notes: Union[str, None] = None
    treatment_outcome: Union[str, None] = None
    treatment_duration: int
    treatment_frequency: Union[str, None] = None
    treatment_location: Union[str, None] = None
    treatment_cost: Union[float, None] = None
    treatment_insurance_coverage: Union[str, None] = None
    treatment_follow_up_plan: Union[str, None] = None
    treatment_date_created: datetime
    treatment_date_updated: Union[datetime, None] = None

class TreatmentCreate(TreatmentBase):
    chief_complaint_id: int
    medical_record_id: int

class Treatment(TreatmentBase):
    treatment_id: int
    chief_complaint_id: int
    medical_record_id: int

class UserActivityLogBase(BaseModel):
    user_date_time_of_activity: datetime
    activity_description: str

class UserActivityLogCreate(UserActivityLogBase):
    user_id: int

class UserActivityLog(UserActivityLogBase):
    user_activity_log_id: int
    user_id: int

class UserAuthorizedFacilityBase(BaseModel):
    facility_id: str

class UserAuthorizedFacilityCreate(UserAuthorizedFacilityBase):
    user_id: int

class UserAuthorizedFacility(UserAuthorizedFacilityBase):
    user_authorized_facility_id: int
    user_id: int

class UserLoginLogBase(BaseModel):
    user_date_time_of_activity: datetime
    activity_description: str

class UserLoginLogCreate(UserLoginLogBase):
    user_id: int

class UserLoginLog(UserLoginLogBase):
    user_login_log_id: int
    user_id: int

class VisitBase(BaseModel):
    visits_title: str
    visits_date: datetime
    visits_description: str

class VisitCreate(VisitBase):
    medical_record_id: int

class Visit(VisitBase):
    visit_id: int
    medical_record_id: int

class VitalBase(BaseModel):
    vitals_date_taken: Union[datetime, None] = None
    vitals_height: Union[float, None] = None
    vitals_weight: Union[float, None] = None
    vitals_calculated_bmi: Union[float, None] = None
    vitals_temperature: Union[float, None] = None
    vitals_pulse: Union[float, None] = None
    vitals_respiratory_rate: Union[float, None] = None
    vitals_blood_pressure_systolic: Union[float, None] = None
    vitals_blood_pressure_diastolic: Union[float, None] = None
    vitals_arterial_blood_oxygen_saturation: Union[float, None] = None

class VitalCreate(VitalBase):
    chief_complaint_id: int
    medical_record_id: int

class Vital(VitalBase):
    vitals_id: int
    chief_complaint_id: int
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