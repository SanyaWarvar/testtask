from pydantic import BaseModel


class MessageScheme(BaseModel):
    message: str
    author: str
