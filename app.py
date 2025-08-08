from flask import Flask, request

app = Flask(__name__)

PAYHERE_MERCHANT_ID = 'YOUR_MERCHANT_ID'
RETURN_URL = 'https://yourdomain.com/return'
CANCEL_URL = 'https://yourdomain.com/cancel'
NOTIFY_URL = 'https://yourdomain.com/notify'

@app.route("/", methods=["GET"])
def index():
    return open("index.html").read()

@app.route("/pay", methods=["POST"])
def pay():
    phone = request.form["phone"]
    amount = request.form["amount"]
    return f"""
    <form method='post' action='https://www.payhere.lk/pay/checkout' id='payForm'>
        <input type='hidden' name='merchant_id' value='{PAYHERE_MERCHANT_ID}'>
        <input type='hidden' name='return_url' value='{RETURN_URL}'>
        <input type='hidden' name='cancel_url' value='{CANCEL_URL}'>
        <input type='hidden' name='notify_url' value='{NOTIFY_URL}'>
        <input type='hidden' name='order_id' value='RELOAD_{phone}'>
        <input type='hidden' name='items' value='Dialog Reload for {phone}'>
        <input type='hidden' name='amount' value='{amount}'>
        <input type='hidden' name='currency' value='LKR'>
        <input type='hidden' name='first_name' value='Quick'>
        <input type='hidden' name='last_name' value='Reload'>
        <input type='hidden' name='email' value='info@quickreload.com'>
        <input type='hidden' name='phone' value='{phone}'>
        <input type='hidden' name='address' value='N/A'>
        <input type='hidden' name='city' value='Colombo'>
        <input type='hidden' name='country' value='Sri Lanka'>
    </form>
    <script>document.getElementById('payForm').submit();</script>
    """

@app.route("/notify", methods=["POST"])
def notify():
    # This is where PayHere sends confirmation after payment
    return "Payment received", 200

if __name__ == "__main__":
    app.run(debug=True)