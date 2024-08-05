import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN")
BASE_API_URL = os.environ.get("BASE_API_URL")
