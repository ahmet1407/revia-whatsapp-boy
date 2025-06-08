from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/message", methods=['POST'])
def message():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()

    if 'dyson' in incoming_msg:
        reply = "Dyson V15 Detect: Tatmin 92, Risk 23, Hissiyat 88, Uzman Skoru 90"
    else:
        reply = "Lütfen analiz etmem için geçerli bir ürün adı gönderin."

    resp.message(reply)
    return str(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
