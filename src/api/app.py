from fastapi import FastAPI
from .routers import router as messages_router

app = FastAPI()
app.include_router(messages_router)
