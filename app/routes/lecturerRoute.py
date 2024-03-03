from fastapi import APIRouter, Depends
from ..pocketbaseCon import pb

router = APIRouter()

@router.get("/api/lecturer")
async def get_lecturers():
    records =  pb.collection("lecturer").get_list()
    return records

@router.get("/api/lecturer/{lecturer_id}")
async def get_lecturer(lecturer_id: str):
    record = pb.collection("lecturer").get_one(lecturer_id)
    return record

@router.post("/api/lecturer")
async def create_lecturer(request: dict):
    record = pb.collection("lecturer").create(request)
    return record

@router.put("/api/lecturer/{lecturer_id}")
async def update_lecturer(lecturer_id: str, request: dict):
    record = pb.collection("lecturer").update(lecturer_id, request)
    return record

@router.delete("/api/lecturer/{lecturer_id}")
async def delete_lecturer(lecturer_id: str):
    record = pb.collection("lecturer").delete(lecturer_id)
    return record

