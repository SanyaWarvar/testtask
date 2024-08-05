from fastapi import APIRouter, HTTPException
from .schemas import MessageScheme
from .db import mdb

router = APIRouter(
    prefix="/api"
)


@router.get("/v1/messages", status_code=200)
async def get_messages():
    return mdb.read_messages()


@router.post("/v1/message", status_code=201)
async def send_message(message: MessageScheme):
    try:
        mdb.insert_message(message.message, message.author)
        return {"details": "Success"}
    except:
        return HTTPException(status_code=400, detail="Error! Try again!")
