
from fastapi import APIRouter
from backend.db import db

router = APIRouter()

# 1. Count violations by type
@router.get("/analytics/violations")
async def count_violations():
    pipeline = [
        {"$unwind": "$incident_details.violation_types"},
        {"$group": {"_id": "$incident_details.violation_types", "count": {"$sum": 1}}}
    ]
    result = await db.incident_reports.aggregate(pipeline).to_list(100)
    return result

# 2. Map visualization data (coordinates + type)
@router.get("/analytics/geodata")
async def geo_data():
    reports = await db.incident_reports.find({}, {"incident_details.location": 1}).to_list(100)
    for r in reports:
        r["_id"] = str(r["_id"])
    return reports

# 3. Time-based report trends
@router.get("/analytics/timeline")
async def timeline():
    pipeline = [
        {"$group": {
            "_id": {"$dateToString": {"format": "%Y-%m", "date": "$created_at"}},
            "count": {"$sum": 1}
        }},
        {"$sort": {"_id": 1}}
    ]
    result = await db.incident_reports.aggregate(pipeline).to_list(100)
    return result
