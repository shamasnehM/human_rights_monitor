from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Victim demographics info
class Demographics(BaseModel):
    gender: str
    age: int
    ethnicity: str
    occupation: str

# Risk assessment information
class RiskAssessment(BaseModel):
    level: str  # e.g., low, medium, high
    threats: List[str]
    protection_needed: bool

# Support services provided
class SupportService(BaseModel):
    type: str  # e.g., legal, medical
    provider: str
    status: str  # e.g., active, pending

# Victim or witness full model
class Victim(BaseModel):
    type: str  # "victim" or "witness"
    anonymous: bool
    demographics: Demographics
    contact_info: Optional[dict]
    cases_involved: List[str]
    risk_assessment: RiskAssessment
    support_services: List[SupportService]
    created_at: datetime
    updated_at: datetime
