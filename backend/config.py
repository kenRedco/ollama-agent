# backend/config.py
import os
from dotenv import load_dotenv
load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")   # sender
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")  # app password or SMTP token
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3")
DRY_RUN = os.getenv("DRY_RUN", "true").lower() == "true"  # safe default
