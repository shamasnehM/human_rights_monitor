
from fastapi import APIRouter, HTTPException, Form
from typing import Optional
from bson import ObjectId
from backend.db import db
from datetime import datetime

router = APIRouter()

# 1. Add a new victim/witness
@router.post("/victims/")
async def add_victim(victim: dict):
    victim["created_at"] = datetime.utcnow()
    result = await db.victims.insert_one(victim)
    return {"inserted_id": str(result.inserted_id)}

# 2. Get victim details (restricted access assumed)
@router.get("/victims/{victim_id}")
async def get_victim(victim_id: str):
    victim = await db.victims.find_one({"_id": ObjectId(victim_id)})
    if not victim:
        raise HTTPException(status_code=404, detail="Victim not found")
    victim["_id"] = str(victim["_id"])
    return victim

# 3. Update victim risk level
@router.patch("/victims/{victim_id}")
async def update_risk(victim_id: str, risk_level: str = Form(...)):
    result = await db.victims.update_one(
        {"_id": ObjectId(victim_id)},
        {"$set": {"risk_assessment.level": risk_level}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Victim not found")
    return {"message": "Risk level updated"}

# 4. List victims linked to a case
@router.get("/victims/case/{case_id}")
async def get_victims_by_case(case_id: str):
    victims = await db.victims.find({"cases_involved": ObjectId(case_id)}).to_list(100)
    for v in victims:
        v["_id"] = str(v["_id"])
    return victims


@router.get("/victims")
async def get_all_victims():
    victims = await db.victims.find().to_list(100)
    for v in victims:
        v["_id"] = str(v["_id"])
    return victims
