from typing import List
from pymongo import MongoClient
from ..config import MONGO_HOST, MONGO_PORT


class MessagesDB:
    def __init__(self, host="localhost", port=27017):
        self.client = MongoClient(host, port)
        self.db = self.client.test

    def read_messages(self) -> List:
        messages = self.db.messages.find({}, {"_id": 0})
        return list(messages)

    def insert_message(self, message: str, author: str):
        self.db.messages.insert_one({
            "text": message,
            "author": author
        })


mdb = MessagesDB(MONGO_HOST, MONGO_PORT)
