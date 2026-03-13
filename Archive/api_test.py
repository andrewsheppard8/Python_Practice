"""GET request
http://127.0.0.1:5000/balance?owner=Andrew
"""

"""POST request
curl -X POST -H "Content-Type: application/json" \
-d '{"owner": "Bob", "amount": 50}' \
http://127.0.0.1:5000/deposit or withdraw
"""

from flask import Flask, request, jsonify
from flask_cors import CORS  # <- import CORS

app = Flask(__name__)
CORS(app)

accounts_data={
    "Andrew":100,
    "Bob":200,
    "Chelsea":300
}

# Endpoint to get balance
@app.route("/balance", methods=["GET"])
def get_balance():
    owner = request.args.get("owner")
    if owner in accounts_data:
        return jsonify({"owner": owner, "balance": accounts_data[owner]})
    else:
        return jsonify({"error": "Account not found"}), 404
    

# Endpoint to deposit
@app.route("/deposit", methods=["POST"])
def deposit():
    data = request.json
    owner = data.get("owner")
    amount = data.get("amount", 0)
    
    if owner not in accounts_data:
        return jsonify({"error": "Account not found"}), 404

    accounts_data[owner] += amount
    return jsonify({"owner": owner, "new_balance": accounts_data[owner]})

# Endpoint to withdraw
@app.route("/withdraw", methods=["POST"])
def withdraw():
    data = request.json
    owner = data.get("owner")
    amount = data.get("amount", 0)
    
    if owner not in accounts_data:
        return jsonify({"error": "Account not found"}), 404
    
    if amount > accounts_data[owner]:
        return jsonify({"error": "Insufficient funds"}), 400
    
    accounts_data[owner] -= amount
    return jsonify({"owner": owner, "new_balance": accounts_data[owner]})

# Run the API
if __name__ == "__main__":
    app.run(debug=True)