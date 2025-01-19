from flask import Flask, request, jsonify
import stripe

# Initialize Flask app
app = Flask(__name__)

# Set your Stripe secret key
stripe.api_key = "API"

# Endpoint to create a customer
@app.route('/webhook/customers', methods=['POST'])
def create_customer():
    data = request.get_json()  # Read JSON input
    try:
        # Use Stripe API to create a customer
        customer = stripe.Customer.create(
            name=data['name'],
            email=data['email']
        )
        return jsonify({"status": "success", "customer_id": customer.id}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

# Endpoint to create a charge
@app.route('/webhook/charges', methods=['POST'])
def create_charge():
    data = request.get_json()  # Read JSON input
    try:
        # Use Stripe API to create a charge
        charge = stripe.Charge.create(
            amount=data['amount'],  # Amount in cents
            currency=data['currency'],
            customer=data['customer_id']
        )
        return jsonify({"status": "success", "charge_id": charge.id}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

# Run the app
if __name__ == '__main__':
    app.run(port=5000)
