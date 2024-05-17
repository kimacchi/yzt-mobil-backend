from typing import Union
from pocketbase import PocketBase
from fastapi import FastAPI
from pydantic import BaseModel
import os

from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


client = PocketBase('https://gazi-yapay-zeka.pockethost.io/')


class Item(BaseModel):
    hello: str
    
    
    
class QRControl(BaseModel):
    type: str
    event: str
    user: str
    session: str # ! 01 02 03 04 05 11 12 13 14 15


# Branch test
@app.get("/")
def read_root():
    return {"Hello": "World again"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):

    return {"item_id": item_id, "q": q}


@app.post("/items/")
async def post_item(item: Item):
    members = client.collection("members").get_full_list()
    return {"item": item.hello, "members": members}


@app.get("/qr-control/")
async def qr_control_get():
    return {"status": "ok"}
    
    
@app.post("/qr-control/")
async def qr_control(item: QRControl):
    if item.type == "ticket":
        try:
            eventToBeControlled = client.collection("events").get_full_list()
            eventToBeControlled = [x for x in eventToBeControlled if x.id == item.event]
            eventToBeControlled = eventToBeControlled[0]
            if [x for x in eventToBeControlled.participants if x == item.user]:
                email = os.environ.get("PB_AUTH_EMAIL")
                password = os.environ.get("PB_AUTH_PASSWORD")
                client.admins.auth_with_password(email, password)

                # ! Add participant to the event to the correct session.
                # * id should be as follows: aisecsecret0{day(0-1)session(1-5)} e.g. aisecsecret011 (first day, first session)
                client.collection("events").update("ai2secsecret0" + item.session, {"participants+": item.user})
                return {"ticketValidation": True}
            return {"ticketValidation": False}
        except:
            return {"ticketValidation": False, "error": "Event not found"}