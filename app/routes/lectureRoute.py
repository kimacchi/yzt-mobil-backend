from fastapi import APIRouter
from ..pocketbaseCon import pb

router = APIRouter()

# Fetch all lectures without pagination
@router.get("/api/lecture")
async def get_lectures():
    records =  pb.collection("lecture").get_list()
    return records

# Fetch a single lecture by its ID
@router.get("/api/lecture/{lecture_id}")
async def get_lecture(lecture_id: str):
    record = pb.collection("lecture").get_one(lecture_id)
    return record

# Create a new lecture
@router.post("/api/lecture")
async def create_lecture(request: dict):
    record = pb.collection("lecture").create(request)
    return record


# Update a lecture by its ID
@router.put("/api/lecture/{lecture_id}")
async def update_lecture(lecture_id: str, request: dict):
    record = pb.collection("lecture").update(lecture_id, request)
    return record

# Delete a lecture by its ID
@router.delete("/api/lecture/{lecture_id}")
async def delete_lecture(lecture_id: str):
    record = pb.collection("lecture").delete(lecture_id)
    return record