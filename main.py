from flask import Flask, request
import requests
import os

app = Flask(__name__)

# --- AYARLAR ---
# Senin Bot Tokenin (Gedza - @Tetris_Alarmbot)
TELEGRAM_BOT_TOKEN = "8380101160:AAE4p3IPm3wKyHliOfxUBMVIJl4i3Jo-Q3o"

# Buraya @userinfobot'tan aldığın kendi ID numaranı yaz (Tırnak içinde kalsın)
TELEGRAM_CHAT_ID = "BURAYA_KENDI_ID_NUMARANI_YAZ"

def telegrama_gonder(mesaj):
    """Sinyali anlık olarak Telegram'a fırlatır."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": mesaj,
        "parse_mode": "HTML"
    }
    try:
        requests.post(url, json=payload, timeout=10)
    except Exception as e:
        print(f"Telegram Hatası: {e}")

@app.route('/webhook', methods=['POST'])
def webhook():
    # TradingView'dan gelen ham veriyi alıyoruz
    data = request.get_data(as_text=True)
    
    # Gelen sinyali güzelleştiriyoruz
    duzenli_mesaj = (
        f"<b>🔔 YENİ RADAR SİNYALİ</b>\n"
        f"━━━━━━━━━━━━━━━\n"
        f"<b>Mesaj:</b> {data}\n"
        f"<b>Zaman:</b> 21 Nisan 2026, 21:17\n"
        f"━━━━━━━━━━━━━━━\n"
        f"🔎 <i>Hemen grafiği kontrol et!</i>"
    )
    
    # Telegram'a gönder
    telegrama_gonder(duzenli_mesaj)
    
    return "TAMAM", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
