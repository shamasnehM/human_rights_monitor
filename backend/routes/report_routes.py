
from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from backend.db import db
import os
import shutil
import uuid

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Helper function to save uploaded files to disk
async def save_files(files: List[UploadFile]) -> List[dict]:
    saved = []
    for file in files:
        ext = os.path.splitext(file.filename)[1]
        unique_name = f"{uuid.uuid4().hex}{ext}"
        file_path = os.path.join(UPLOAD_DIR, unique_name)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        saved.append({
            "type": file.content_type.split("/")[0],
            "url": f"/{UPLOAD_DIR}/{unique_name}",
            "description": file.filename
        })
    return saved

# 1. Submit a new incident report with file uploads
@router.post("/reports/")
async def submit_report_with_files(
    reporter_type: str = Form(...),
    anonymous: bool = Form(...),
    email: Optional[str] = Form(None),
    phone: Optional[str] = Form(None),
    preferred_contact: Optional[str] = Form(None),
    date: str = Form(...),
    country: str = Form(...),
    city: str = Form(...),
    lat: float = Form(...),
    lon: float = Form(...),
    description: str = Form(...),
    violation_types: str = Form(...),  # comma-separated
    files: List[UploadFile] = File(default=[])
):
    contact_info = None
    if not anonymous:
        contact_info = {
            "email": email,
            "phone": phone,
            "preferred_contact": preferred_contact
        }

    evidence = await save_files(files)
    report = {
        "report_id": f"IR-{uuid.uuid4().hex[:8]}",
        "reporter_type": reporter_type,
        "anonymous": anonymous,
        "contact_info": contact_info,
        "incident_details": {
            "date": datetime.fromisoformat(date),
            "location": {
                "country": country,
                "city": city,
                "coordinates": {
                    "type": "Point",
                    "coordinates": [lon, lat]
                }
            },
            "description": description,
            "violation_types": violation_types.split(",")
        },
        "evidence": evidence,
        "status": "new",
        "assigned_to": None,
        "created_at": datetime.utcnow()
    }

    result = await db.incident_reports.insert_one(report)
    return {"inserted_id": str(result.inserted_id)}

# 2. Retrieve reports with optional filters (status, city, date range)
@router.get("/reports/")
async def list_reports(
    status: Optional[str] = None,
    city: Optional[str] = None,
    date_from: Optional[str] = None,
    date_to: Optional[str] = None
):
    query = {}
    if status:
        query["status"] = status
    if city:
        query["incident_details.location.city"] = city
    if date_from or date_to:
        date_query = {}
        if date_from:
            date_query["$gte"] = datetime.fromisoformat(date_from)
        if date_to:
            date_query["$lte"] = datetime.fromisoformat(date_to)
        query["incident_details.date"] = date_query

    reports = await db.incident_reports.find(query).to_list(100)
    for r in reports:
        r["_id"] = str(r["_id"])
    return reports

# 3. Update the status of a report
@router.patch("/reports/{report_id}")
async def update_report_status(report_id: str, new_status: str = Form(...)):
    result = await db.incident_reports.update_one(
        {"_id": ObjectId(report_id)},
        {"$set": {"status": new_status}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Report not found")
    return {"message": "Report status updated successfully"}

# 4. Return violation count grouped by type
@router.get("/reports/analytics")
async def get_violation_analytics():
    pipeline = [
        {"$unwind": "$incident_details.violation_types"},
        {"$group": {"_id": "$incident_details.violation_types", "count": {"$sum": 1}}}
    ]
    result = await db.incident_reports.aggregate(pipeline).to_list(100)
    return result
