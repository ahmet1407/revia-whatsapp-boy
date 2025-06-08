from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def message():
    incoming_msg = request.values.get('Body', '').lower()
    if 'dyson' in incoming_msg:
        return jsonify({'response': 'Dyson V15 Detect: Tatmin 92, Risk 23, Hissiyat 88, Uzman Skoru 90'})
    else:
        return jsonify({'response': 'Üzgünüm, bu ürün için henüz bir değerlendirme yok.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))