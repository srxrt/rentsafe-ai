# config.py
import os


class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    INSTRUCTIONS = "You are a coding assistant that talks like a pirate."
