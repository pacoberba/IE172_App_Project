from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/view-transaction/<transaction_number>')
def view_transaction(transaction_number):
    # Placeholder data for the transaction details
    transaction_info = {
        "transaction_number": transaction_number,
        "client_name": "Jose Rizal",
        "client_id": "C123456789",
        "transaction_type": "Adoption"
    }

    payment_info = {
        "transaction_id": "TX987654321",
        "application_number": "APP123456",
        "payment_amount": "PHP 5000",
        "payment_mode": "Bank Transfer",
        "proof_of_payment": "Yes"
    }

    # HTML code with integrated Python for displaying the information
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>View Transaction: No. {{ transaction_number }}</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
            }
            h2 {
                color: #333;
                margin-top: 30px;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 10px;
            }
            th, td {
                padding: 10px;
                text-align: left;
                border: 1px solid #ddd;
            }
            th {
                background-color: #f2f2f2;
            }
            button {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                cursor: pointer;
            }
            button:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <h2>VIEW TRANSACTION: No. {{ transaction_number }}</h2>

        <h3>TRANSACTION INFORMATION</h3>
        <table>
            <tr><th>Transaction Number</th><td>{{ transaction_info.transaction_number }}</td></tr>
            <tr><th>Client Name</th><td>{{ transaction_info.client_name }}</td></tr>
            <tr><th>Client ID</th><td>{{ transaction_info.client_id }}</td></tr>
            <tr><th>Transaction Type</th><td>{{ transaction_info.transaction_type }}</td></tr>
        </table>

        <h3>PAYMENT INFORMATION</h3>
        <table>
            <tr><th>Transaction ID</th><td>{{ payment_info.transaction_id }}</td></tr>
            <tr><th>Application Number</th><td>{{ payment_info.application_number }}</td></tr>
            <tr><th>Payment Amount</th><td>{{ payment_info.payment_amount }}</td></tr>
            <tr><th>Payment Mode</th><td>{{ payment_info.payment_mode }}</td></tr>
            <tr><th>Proof of Payment</th><td>{{ payment_info.proof_of_payment }}</td></tr>
        </table>

        <h3>VERIFICATION</h3>
        <p>Would you like to tag this transaction as verified?</p>
        <form action="/verify-transaction/{{ transaction_number }}" method="post">
            <button type="submit">Verify</button>
        </form>

    </body>
    </html>
    """, transaction_number=transaction_number, transaction_info=transaction_info, payment_info=payment_info)

@app.route('/verify-transaction/<transaction_number>', methods=['POST'])
def verify_transaction(transaction_number):
    # Here you can add logic to verify the transaction (e.g., updating the database)
    return f"Transaction {transaction_number} has been verified!"

