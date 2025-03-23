# config.py
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    INSTRUCTIONS = "you are a normal person"
