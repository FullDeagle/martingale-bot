import os
import requests
from dotenv import load_dotenv

load_dotenv()

TG_TOKEN = os.getenv("TG_TOKEN")
TG_CHAT  = os.getenv("TG_CHAT")

def tg(msg: str):
    """Отправить сообщение в Telegram"""
    if not TG_TOKEN or not TG_CHAT:
        print("TG not configured:", msg)
        return
    url = f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage"
    try:
        requests.post(url, data={"chat_id": TG_CHAT, "text": msg})
    except Exception as e:
        print("Failed to send TG:", e)
