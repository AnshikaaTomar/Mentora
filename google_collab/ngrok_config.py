import os
from pyngrok import ngrok

def start_ngrok(port=8000):
    NGROK_TOKEN = os.environ.get("NGROK_AUTH_TOKEN")
    if NGROK_TOKEN is None:
        raise ValueError("❌ NGROK_AUTH_TOKEN not set in environment")
    ngrok.set_auth_token(NGROK_TOKEN)
    tunnel = ngrok.connect(port)
    return tunnel
