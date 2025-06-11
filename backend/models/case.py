from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from enum import Enum

# Enum for case status
class CaseStatus(str, Enum):
    new = "new"
    under_investigation = "under_investigation"
    resolved = "resolved"
    archived = "archived"

# Enum for priority level
class PriorityLevel(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

# Location information
class Location(BaseModel):
    country: str
    region: Optional[str]
    coordinates: dict  # Expected to be GeoJSON: {"type": "Point", "coordinates": [lon, lat]}

# Evidence attached to the case
class Evidence(BaseModel):
    type: str
    url: str
    description: str
    date_captured: Optional[datetime]

# Main Case model
class Case(BaseModel):
    case_id: str
    title: str
    description: str
    violation_types: List[str]
    status: CaseStatus = CaseStatus.new
    priority: PriorityLevel
    location: Location
    date_occurred: datetime
    date_reported: datetime
    victims: List[str]
    perpetrators: List[dict]
    evidence: List[Evidence]
    created_by: Optional[str]
    created_at: datetime
    updated_at: datetime

# Optional: Track changes to case status
class CaseStatusHistory(BaseModel):
    case_id: str
    previous_status: str
    updated_status: str
    updated_at: datetime
    updated_by: str
