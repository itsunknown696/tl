import os

API_ID    = os.environ.get("API_ID", "27238809")
API_HASH  = os.environ.get("API_HASH", "c854867f7b27f65aebd41392eb2af1d9")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7612317086:AAFl0__l2Gy-UAdrqOlCb1j_Y_NFCu8qUpw") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
