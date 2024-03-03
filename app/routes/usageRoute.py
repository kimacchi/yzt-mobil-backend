from fastapi import APIRouter, Depends
from ..pocketbaseCon import pb

router = APIRouter()


@router.get("/api/usage")
async def get_usages():
    records = pb.collection("usage").get_list()
    return records

@router.get("/api/usage/{usage_id}")
async def get_usage(usage_id: str):
    record = pb.collection("usage").get_one(usage_id)
    return record

@router.post("/api/usage")
async def create_usage(request: dict):
    record = pb.collection("usage").create(request)
    return record

@router.put("/api/usage/{usage_id}")
async def update_usage(usage_id: str, request: dict):
    record = pb.collection("usage").update(usage_id, request)
    return record

@router.delete("/api/usage/{usage_id}")
async def delete_usage(usage_id: str):
    record = pb.collection("usage").delete(usage_id)
    return record