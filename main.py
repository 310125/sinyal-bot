from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_data(as_text=True)
    print(f"Sinyal Geldi: {data}")
    return 'TAMAM', 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
