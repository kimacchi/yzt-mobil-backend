from fastapi import APIRouter
from ..pocketbaseCon import pb

router = APIRouter()

# Fetch all classes
@router.get("/api/class")
async def get_classes():
    records =  pb.collection("class").get_list()
    return records
    
# Fetch a single class by its ID
@router.get("/api/class/{class_id}")
async def get_class(class_id: str):
    record = pb.collection("class").get_one(class_id)
    return record
    

# Create a new class
@router.post("/api/class")
async def create_class(request: dict):
    record = pb.collection("class").create(request)
    return record

# Update a class by its ID
@router.put("/api/class/{class_id}")
async def update_class(class_id: str, request: dict):
    record = pb.collection("class").update(class_id, request)
    return record

# Delete a class by its ID
@router.delete("/api/class/{class_id}")
async def delete_class(class_id: str):
    record = pb.collection("class").delete(class_id)
    return record

# Fetch classes with pagination and filtering
# @router.get("/api/class/filter")
# async def get_classes_filtered(page: int = 1, per_page: int = 30, filter_str: str = ""):
#     print("page:", page, "per_page:", per_page, "filter:", filter_str)
#     # records = pb.collection("class").get_list(page=page, per_page=per_page, filter=filter)
#     # return records
#     dict_ = {"page": page, "per_page": per_page, "filter": filter_str}
#     return dict_