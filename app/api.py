from typing import Union
from pocketbase import PocketBase
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


client = PocketBase('https://gazi-yapay-zeka.pockethost.io/')


class Item(BaseModel):
    hello: str
    
    
    
class QRControl(BaseModel):
    type: str
    event: str
    user: str


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
            # return {"event": eventToBeControlled}
            if [x for x in eventToBeControlled.participants if x == item.user]:
                return {"ticketValidation": True}
            return {"ticketValidation": False}
        except:
            return {"ticketValidation": False, "error": "Event not found"}