from typing import Union
from pydantic import BaseModel

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
    pass

