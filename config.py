import os
from dotenv import load_dotenv
from helpers import str_to_int_from_env

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
ADMINS = str_to_int_from_env(os.getenv("ADMINS"))