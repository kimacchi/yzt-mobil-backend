from typing import Union

from fastapi import FastAPI

from .routes import test, lectureRoute, lecturerRoute, classRoute, suggestionRoute, usageRoute
from .pocketbaseCon import pb

app = FastAPI()

@app.get("/api/")
def read_root():
    return {"Hello": "World again"}

app.include_router(test.router)
app.include_router(lecturerRoute.router)
app.include_router(lectureRoute.router)
app.include_router(classRoute.router)
app.include_router(suggestionRoute.router)
app.include_router(usageRoute.router)