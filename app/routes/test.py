from fastapi import APIRouter
# from pocketbase import PocketBase

# pb = PocketBase("http://127.0.0.1:8090/")

# authData = pb.admins.auth_with_password("mahmutenesdevsec@gmail.com","Deneme1234")

from ..pocketbaseCon import pb

router = APIRouter()

@router.get("/")
async def test():
    return {"Hello": "From test route"}
