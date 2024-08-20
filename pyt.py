from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/paypal-webhook', methods=['POST'])
def paypal_webhook():
    try:
        data = request.get_json()
        # Logica pentru procesarea webhook-ului
        print('Received webhook data:', data)
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        print('Error processing webhook:', e)
        return jsonify({'status': 'error'}), 500

@app.route('/')
def index():
    return 'Welcome to the webhook endpoint!', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
