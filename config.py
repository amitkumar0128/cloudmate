# config.py
from dotenv import load_dotenv
import os

load_dotenv()  # This reads .env from the root directory

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
PROMETHEUS_SECRET = os.getenv("PROMETHEUS_SECRET")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

ENDPOINTS = [
    "https://api.github.com",
    "https://aws.amazon.com",
    "https://status.yourservice.com"
]
