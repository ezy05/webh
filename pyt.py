from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/paypal-webhook', methods=['POST'])
def paypal_webhook():
    data = request.json
    print('Received webhook event:', data)
    return jsonify(status='success'), 200

if __name__ == '__main__':
    app.run(port=3000)
