
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Coordinates(BaseModel):
    type: str = "Point"
    coordinates: List[float]  # [longitude, latitude]

class Location(BaseModel):
    country: str
    city: str
    coordinates: Coordinates

class IncidentDetails(BaseModel):
    date: datetime
    location: Location
    description: str
    violation_types: List[str]

class Evidence(BaseModel):
    type: str
    url: str
    description: str

class Report(BaseModel):
    report_id: str
    reporter_type: str
    anonymous: bool
    contact_info: Optional[dict]
    incident_details: IncidentDetails
    evidence: List[Evidence]
    status: str
    assigned_to: Optional[str]
    created_at: datetime
