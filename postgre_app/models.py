from sqlalchemy import Column, Boolean, ForeignKey, Integer, BigInteger, Double, String
from sqlalchemy.orm import relationship
from datetime import date, datetime
from database import Base

class Admission(Base):
    __tablename__ = "admissions"

    admission_id = Column(BigInteger, primary_key=True, nullable=False)
    medical_record_id = Column(BigInteger, ForeignKey("medical_records.medical_record_id"), nullable=False)
    date_of_admission = Column(datetime, nullable=False)
    admissions_description = Column(String, nullable=False)

    medical_record = relationship("MedicalRecord", back_populates="admission")

class Allergy(Base):
    __tablename__ = "allergies"

    allergy_id = Column(BigInteger, primary_key=True, nullable=False)
    medical_record_id = Column(BigInteger, ForeignKey("medical_records.medical_record_id"), nullable=False)
    allergy_name = Column(String(75), nullable=False)
    allergy_severity = Column(String(75))
    additional_information = Column(String)

    medical_record = relationship("MedicalRecord", back_populates="allergy")

class Appointment(Base):
    __tablename__ = "appointments"

    appointment_id = Column(BigInteger, primary_key=True, nullable=False)
    medical_record_id = Column(BigInteger, ForeignKey("medical_records.medical_record_id"), nullable=False)
    appointment_title = Column(String(75), nullable=False)
    appointment_date = Column(datetime, nullable=False)
    appointment_description = Column(String, nullable=False)

    medical_record = relationship("MedicalRecord", back_populates="appointment")

class Assessment(Base):
    __tablename__ = "assessments"

    assessment_id = Column(BigInteger, primary_key=True, nullable=False)
    chief_complaint_id = Column(BigInteger, ForeignKey("chief_complaints.chief_complaint_id"), nullable=False)
    medical_record_id = Column(BigInteger, ForeignKey("medical_records.medical_record_id"), nullable=False)
    assessments_summation = Column(String, nullable=False)

    chief_complaint = relationship("ChiefComplaint", back_populates="assessment")
    medical_record = relationship("MedicalRecord", back_populates="assessment")

class BloodRelative(Base):
    __tablename__ = "blood_relatives"

    blood_relatives_id = Column(BigInteger, primary_key=True, nullable=False)
    medical_record_id = Column(BigInteger, ForeignKey("medical_records.medical_record_id"), nullable=False)
    mother_status = Column(String(45), nullable=False)
    father_status = Column(String(45), nullable=False)
    mother_deceased_age = Column(Integer)
    father_deceased_age = Column(Integer)
    num_sisters_alive = Column(Integer, nullable=False)
    num_brothers_alive = Column(Integer, nullable=False)
    num_daughters_alive = Column(Integer, nullable=False)
    num_sons_alive = Column(Integer, nullable=False)
    mother_cause_of_death = Column(String)
    father_cause_of_death = Column(String)

    medical_record = relationship("MedicalRecord", back_populates="blood_relative")

class ChiefComplaint(Base):
    __tablename__ = "chief_complaints"

    chief_complaint_id = Column(BigInteger, primary_key=True, nullable=False)
    medical_record_id = Column(BigInteger, ForeignKey("medical_records.medical_record_id"), nullable=False)
    chief_complaint_statement = Column(String, nullable=False)
    chief_complaint_date = Column(datetime, nullable=False)

    medication = relationship("Medication", back_populates="chief_complaint")
    surgical_related_problem = relationship("SurgicalRelatedProblem", back_populates="chief_complaint")
    vital = relationship("Vital", back_populates="chief_complaint")
    treatment = relationship("Treatment", back_populates="chief_complaint")
    review_of_systems = relationship("ReviewOfSystems", back_populates="chief_complaint")
    physical_exam = relationship("PhysicalExam", back_populates="chief_complaint")
    assessment = relationship("Assessment", back_populates="chief_complaint")
    plan = relationship("Plan", back_populates="chief_complaint")
    history_present_illness = relationship("HistoryPresentIllness", back_populates="chief_complaint")
    diagnosis = relationship("Diagnosis", back_populates="chief_complaint")

class Diagnosis(Base):
    __tablename__ = "diagnoses"
    diagnosis_id = Column(BigInteger, primary_key=True, nullable=False)
    chief_complaint_id = Column(BigInteger, ForeignKey("chief_complaints.chief_complaint_id"), nullable=False)
    medical_record_id = Column(BigInteger, ForeignKey("medical_records.medical_record_id"), nullable=False)
    diagnosis_title = Column(String(45), nullable=False)
    diagnosis_date = Column(datetime, nullable=False)
    diagnosis_description = Column(String, nullable=False)

    chief_complaint = relationship("ChiefComplaint", back_populates="diagnosis")
    medical_record = relationship("MedicalRecord", back_populates="diagnosis")

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

class FamilyIllness(Base):
    __tablename__ = "family_illnesses"

    family_illness_id = Column(BigInteger, primary_key=True, nullable=False)
    medical_record_id = Column(BigInteger, ForeignKey("medical_records.medical_record_id"), nullable=False)
    illness = Column(String(75), nullable=False)
    father = Column(Boolean)
    mother = Column(Boolean)
    brothers = Column(Boolean)
    sisters = Column(Boolean)
    sons = Column(Boolean)
    daughters = Column(Boolean)
    grandparents = Column(Boolean)

    medical_record = relationship("MedicalRecord", back_populates="family_illness")

class HistoryPresentIllness(Base):
    __tablename__ = "histories_present_illness"

    history_present_illness_id = Column(BigInteger, primary_key=True, nullable=False)
    chief_complaint_id = Column(BigInteger, ForeignKey("chief_complaints.chief_complaint_id"), nullable=False)
    medical_record_id = Column(BigInteger, ForeignKey("medical_records.medical_record_id"), nullable=False)
    hpi_location = Column(String)
    hpi_character = Column(String)
    hpi_duration = Column(String)
    hpi_onset = Column(String)
    hpi_modifying_factors = Column(String)
    hpi_radiation = Column(String)
    hpi_temporal_pattern = Column(String)
    hpi_severity = Column(String)
    hpi_description = Column(String)

    chief_complaint = relationship("ChiefComplaint", back_populates="history_present_illness")
    medical_record = relationship("MedicalRecord", back_populates="history_present_illness")

class Illness(Base):
    __tablename__ = "illnesses"

    illness_id = Column(BigInteger, primary_key=True, nullable=False)
    chief_complaint_id = Column(BigInteger, ForeignKey("chief_complaints.chief_complaint_id"), nullable=False)
    medical_record_id = Column(BigInteger, ForeignKey("medical_records.medical_record_id"), nullable=False)
    illnesses_diagnosis_date = Column(datetime)
    illnesses_diagnosis_id = Column(BigInteger)
    illnesses_treatment_id = Column(BigInteger)
    illnesses_medication_id = Column(BigInteger)
    illnesses_surgical_related_problem_id = Column(BigInteger)
    illnesses_allergy_id = Column(BigInteger)

    chief_complaint = relationship("ChiefComplaint", back_populates="illness")
    medical_record = relationship("MedicalRecord", back_populates="illness")

class Immunization(Base):
    __tablename__ = "immunizations"

    immunization_id = Column(BigInteger, primary_key=True, nullable=False)
    medical_record_id = Column(BigInteger, ForeignKey("medical_records.medical_record_id"), nullable=False)
    immunization = Column(String(85), nullable=False)

    medical_record = relationship("MedicalRecord", back_populates="immunization")

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
    appointment = relationship("Appointment", back_populates="medical_record")
    family_illness = relationship("FamilyIllness", back_populates="medical_record")
    medication = relationship("Medication", back_populates="medical_record")
    blood_relative = relationship("BloodRelative", back_populates="medical_record")
    visit = relationship("Visit", back_populates="medical_record")
    allergy = relationship("Allergy", back_populates="medical_record")
    immunization = relationship("Immunization", back_populates="medical_record")
    surgical_related_problem = relationship("SurgicalRelatedProblem", back_populates="medical_record")
    admission = relationship("Admission", back_populates="medical_record")
    vital = relationship("Vital", back_populates="medical_record")
    treatment = relationship("Treatment", back_populates="medical_record")
    review_of_systems = relationship("ReviewOfSystems", back_populates="medical_record")
    physical_exam = relationship("PhysicalExam", back_populates="medical_record")
    assessment = relationship("Assessment", back_populates="medical_record")
    plan = relationship("Plan", back_populates="medical_record")
    history_present_illness = relationship("HistoryPresentIllness", back_populates="medical_record")
    diagnosis = relationship("Diagnosis", back_populates="medical_record")

class Medication(Base):
    __tablename__ = "medications"

    medication_id = Column(BigInteger, primary_key=True, nullable=False)
    chief_complaint_id = Column(BigInteger, ForeignKey("chief_complaints.chief_complaint_id"))
    medical_record_id = Column(BigInteger, ForeignKey("medical_records.medical_record_id"), nullable=False)
    medication_name = Column(String(150), nullable=False)
    medication_is_current = Column(Boolean, nullable=False)
    medication_description = Column(String)
    medication_frequency = Column(String(75))
    medication_dosage = Column(Double)
    medication_start_date = Column(datetime)
    medication_end_date = Column(datetime)
    medication_healthcare_provider = Column(String(105))

    chief_complaint = relationship("ChiefComplaint", back_populates="medication")
    medical_record = relationship("MedicalRecord", back_populates="medication")

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

class PhysicalExam(Base):
    __tablename__ = "physical_exams"

    physical_exam_id = Column(BigInteger, primary_key=True, nullable=False)
    chief_complaint_id = Column(BigInteger, ForeignKey("chief_complaints.chief_complaint_id"), nullable=False)
    medical_record_id = Column(BigInteger, ForeignKey("medical_records.medical_record_id"), nullable=False)
    physical_exam_heent = Column(String)
    physical_exam_respiratory = Column(String)
    physical_exam_cardiovascular = Column(String)
    physical_exam_abdominal = Column(String)
    physical_exam_limbs = Column(String)
    physical_exam_neurological = Column(String)
    physical_exam_date = Column(datetime, nullable=False)

    chief_complaint = relationship("ChiefComplaint", back_populates="physical_exam")
    medical_record = relationship("MedicalRecord", back_populates="physical_exam")

class PhysicianAssignedPatient(Base):
    __tablename__ = "physician_assigned_patients"

    staff_user_id = Column(BigInteger, ForeignKey("users.user_id"), nullable=False)
    patient_user_id = Column(BigInteger, nullable=False)

    user = relationship("User", back_populates="physician_assigned_patient")

class Plan(Base):
    __tablename__ = "plans"

    plan_id = Column(BigInteger, primary_key=True, nullable=False)
    chief_complaint_id = Column(BigInteger, ForeignKey("chief_complaints.chief_complaint_id"), nullable=False)
    medical_record_id = Column(BigInteger, ForeignKey("medical_records.medical_record_id"), nullable=False)
    plans_summation = Column(String)

    chief_complaint = relationship("ChiefComplaint", back_populates="plan")
    medical_record = relationship("MedicalRecord", back_populates="plan")

class ReviewOfSystems(Base):
    __tablename__ = "review_of_systems"

    review_of_systems_id = Column(BigInteger, primary_key=True, nullable=False)
    chief_complaint_id = Column(BigInteger, ForeignKey("chief_complaints.chief_complaint_id"), nullable=False)
    medical_record_id = Column(BigInteger, ForeignKey("medical_records.medical_record_id"), nullable=False)
    review_of_systems_constitutional_symptoms = Column(String)
    review_of_systems_eyes = Column(String)
    review_of_systems_ears_nose_throat = Column(String)
    review_of_systems_cardiovascular = Column(String)
    review_of_systems_respiratory = Column(String)
    review_of_systems_gastrointestinal = Column(String)
    review_of_systems_genitournary = Column(String)
    review_of_systems_musculoskeletal = Column(String)
    review_of_systems_integumentary = Column(String)
    review_of_systems_neurological = Column(String)
    review_of_systems_psychiatric = Column(String)
    review_of_systems_endocrine = Column(String)
    review_of_systems_hematologic_lymphatic = Column(String)
    review_of_systems_allergic_immunologic = Column(String)
    review_of_systems_date = Column(datetime)

    chief_complaint = relationship("ChiefComplaint", back_populates="review_of_systems")
    medical_record = relationship("MedicalRecord", back_populates="review_of_systems")

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

class SurgicalRelatedProblem(Base):
    __tablename__ = "surgical_related_problems"

    surgical_related_problem_id = Column(BigInteger, primary_key=True, nullable=False)
    chief_complaint_id = Column(BigInteger, ForeignKey("chief_complaints.chief_complaint_id"), nullable=False)
    medical_record_id = Column(BigInteger, ForeignKey("medical_records.medical_record_id"), nullable=False)
    surgical_related_problem = Column(String(105), nullable=False)
    surgical_related_problem_area = Column(String(75), nullable=False)
    surgicalsurgical_related_problem_procedure = Column(String(225))
    surgical_related_problem_procedure_year = Column(date)

    chief_complaint = relationship("ChiefComplaint", back_populates="surgical_related_problem")
    medical_record = relationship("MedicalRecord", back_populates="surgical_related_problem")

class Treatment(Base):
    __tablename__ = "treatments"

    treatment_id = Column(BigInteger, primary_key=True, nullable=False)
    chief_complaint_id = Column(BigInteger, ForeignKey("chief_complaints.chief_complaint_id"), nullable=False)
    medical_record_id = Column(BigInteger, ForeignKey("medical_records.medical_record_id"), nullable=False)
    treatment_healthcare_provider = Column(String(105))
    treatment_type = Column(String(75), nullable=False)
    treatment_description = Column(String)
    treatment_notes = Column(String)
    treatment_outcome = Column(String(105))
    treatment_duration = Column(Integer, nullable=False)
    treatment_frequency = Column(String(75))
    treatment_location = Column(String(75))
    treatment_cost = Column(Double)
    treatment_insurance_coverage = Column(String)
    treatment_follow_up_plan = Column(String)
    treatment_date_created = Column(datetime, nullable=False)
    treatment_date_updated = Column(datetime)

    chief_complaint = relationship("ChiefComplaint", back_populates="treatment")
    medical_record = relationship("MedicalRecord", back_populates="treatment")

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

class Visit(Base):
    __tablename__ = "visits"

    visit_id = Column(BigInteger, primary_key=True, nullable=False)
    medical_record_id = Column(BigInteger, nullable=False)
    visits_title = Column(String(75), nullable=False)
    visits_date = Column(datetime, nullable=False)
    visits_description = Column(String, nullable=False)

    medical_record = relationship("MedicalRecord", back_populates="visit")

class Vital(Base):
    __tablename__ = "vitals"

    vitals_id = Column(BigInteger, primary_key=True, nullable=False)
    chief_complaint_id = Column(BigInteger, ForeignKey("chief_complaints.chief_complaint_id"), nullable=False)
    medical_record_id = Column(BigInteger, ForeignKey("medical_records.medical_record_id"), nullable=False)
    vitals_date_taken = Column(datetime)
    vitals_height = Column(Double)
    vitals_weight = Column(Double)
    vitals_calculated_bmi = Column(Double)
    vitals_temperature = Column(Double)
    vitals_pulse = Column(Double)
    vitals_respiratory_rate = Column(Double)
    vitals_blood_pressure_systolic = Column(Double)
    vitals_blood_pressure_diastolic = Column(Double)
    vitals_arterial_blood_oxygen_saturation = Column(Double)

    chief_complaint = relationship("ChiefComplaint", back_populates="vital")
    medical_record = relationship("MedicalRecord", back_populates="vital")