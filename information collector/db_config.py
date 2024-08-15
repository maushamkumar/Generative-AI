# db_config.py

from pymongo import MongoClient
import urllib.parse
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client['chatbot_db']
collection = db['users']

def create_user_document(name, email, mobile_number, pdf_filename):
    return {
        "name": name,
        "email": email,
        "mobile_number": mobile_number,
        "pdf_filename": pdf_filename
    }
