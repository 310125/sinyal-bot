from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    gelen_mesaj = request.get_data(as_text=True)
    print(f"Gelen Sinyal: {gelen_mesaj}")

    # 1. YATAY DESTEK DURUMU
    if "PASEU_YATAY_DESTEK_AL" in gelen_mesaj:
        print("🚨 BİLGİ: PASEU Yatay Desteğe Çarptı!")
        print("💰 EYLEM: Borsaya ALIM emri gönderiliyor...")

    # 2. TREND DESTEĞİ DURUMU (YENİ EKLENEN)
    elif "PASEU_TREND_DESTEK_AL" in gelen_mesaj:
        print("📈 BİLGİ: PASEU Yükselen Trend Desteğine Çarptı!")
        print("💰 EYLEM: Trend onayı alındı, Borsaya ALIM emri gönderiliyor...")

    else:
        print("Bilinmeyen bir sinyal geldi, işlem yapılmadı.")

    return 'TAMAM', 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
