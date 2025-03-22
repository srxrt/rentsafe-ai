# config.py
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    INSTRUCTIONS = "You are an AI that analyzes house rental contracts, extracting key details like tenant and landlord info, lease terms, rent amount, property details, and special clauses or conditions, and providing a structured summary."
