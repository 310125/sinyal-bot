from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def ana_sayfa():
    return "✅ Keskin Nisanci Sunucusu Aktif ve Dinlemede!"

@app.route('/tv-sinyal', methods=['POST'])
def sinyal_yakala():
    if request.method == 'POST':
        data = request.json
        if data:
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("🚀 DIKKAT! YENI SINYAL YAKALANDI!")
            print(f"📈 Hisse/Coin : {data.get('ticker')}")
            print(f"💰 Fiyat      : {data.get('price')}")
            print(f"🎯 Aksiyon    : {data.get('action')}")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
            return jsonify({"status": "success", "message": "Sinyal alindi"}), 200
        else:
            return jsonify({"status": "error", "message": "Bos veri"}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
