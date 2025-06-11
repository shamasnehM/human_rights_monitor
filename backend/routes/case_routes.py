
from fastapi import APIRouter, HTTPException, Form
from typing import Optional
from datetime import datetime
from bson import ObjectId
from backend.db import db

router = APIRouter()

# 1. Create a new case
@router.post("/cases/")
async def create_case(case: dict):
    case["created_at"] = datetime.utcnow()
    result = await db.cases.insert_one(case)
    return {"inserted_id": str(result.inserted_id)}

# 2. Get a specific case by ID
@router.get("/cases/{case_id}")
async def get_case(case_id: str):
    case = await db.cases.find_one({"_id": ObjectId(case_id)})
    if not case:
        raise HTTPException(status_code=404, detail="Case not found")
    case["_id"] = str(case["_id"])
    return case

# 3. List all cases with optional filters
@router.get("/cases/")
async def list_cases(status: Optional[str] = None, region: Optional[str] = None):
    query = {}
    if status:
        query["status"] = status
    if region:
        query["location.region"] = region
    cases = await db.cases.find(query).to_list(100)
    for c in cases:
        c["_id"] = str(c["_id"])
    return cases

# 4. Update case status
@router.patch("/cases/{case_id}")
async def update_case_status(case_id: str, new_status: str = Form(...)):
    result = await db.cases.update_one(
        {"_id": ObjectId(case_id)},
        {"$set": {"status": new_status}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Case not found")
    return {"message": "Case status updated"}

# 5. Delete (archive) a case
@router.delete("/cases/{case_id}")
async def delete_case(case_id: str):
    result = await db.cases.delete_one({"_id": ObjectId(case_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Case not found")
    return {"message": "Case archived"}
