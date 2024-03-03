from fastapi import APIRouter, Depends
from ..pocketbaseCon import pb

router = APIRouter()

@router.get("/api/suggestion")
async def get_suggestions():
    records = pb.collection("suggestion").get_list()
    return records

@router.get("/api/suggestion/{suggestion_id}")
async def get_suggestion(suggestion_id: str):
    record = pb.collection("suggestion").get_one(suggestion_id)
    return record

@router.post("/api/suggestion")
async def create_suggestion(request: dict):
    record = pb.collection("suggestion").create(request)
    return record

@router.put("/api/suggestion/{suggestion_id}")
async def update_suggestion(suggestion_id: str, request: dict):
    record = pb.collection("suggestion").update(suggestion_id, request)
    return record

@router.delete("/api/suggestion/{suggestion_id}")
async def delete_suggestion(suggestion_id: str):
    record = pb.collection("suggestion").delete(suggestion_id)
    return record