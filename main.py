from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Reemplaza esto con tu propio token y chat_id
TELEGRAM_BOT_TOKEN = "7930716606:AAHTdFNo7nvgAW7k_Mz_opEc6_wIW3u3S4w"
CHAT_ID = "5458901688"

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=data)

@app.route("/", methods=["GET"])
def home():
    return "Bot de Telegram para Mercado Libre está activo 🚀"

@app.route("/", methods=["POST"])
def meli_webhook():
    data = request.json
    send_telegram_message(f"📬 Nueva notificación de Mercado Libre:\n{data}")
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Bot is running!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render asigna el puerto
    app.run(host="0.0.0.0", port=port)
