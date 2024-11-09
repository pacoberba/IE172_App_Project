from flask import Flask, request

app = Flask(__name__)

# Sample data for transaction histories
transactions = [
    {
        "transaction_id": "TX12345",
        "view_payment": "Link",
        "client_name": "Chito Miranda",
        "transaction_type": "Adoption Fee",
        "date_of_payment": "2024-01-15",
        "amount_paid": "Php 11350",
        "payment_method": "Credit Card",
        "payment_status": "Completed"
    },
    {
        "transaction_id": "TX67890",
        "view_payment": "Link",
        "client_name": "Angel Locsin",
        "transaction_type": "Donation",
        "date_of_payment": "2024-02-10",
        "amount_paid": "Php 200000",
        "payment_method": "PayPal",
        "payment_status": "Pending"
    },
    # Add more sample transactions as needed
]

@app.route('/')
def index():
    # Retrieve search query from URL parameters (if any)
    query = request.args.get('search', '').lower()
    if query:
        # Filter transactions based on search query
        filtered_transactions = [
            tx for tx in transactions if query in tx['transaction_id'].lower() or
            query in tx['client_name'].lower()
        ]
    else:
        filtered_transactions = transactions

    # HTML code with integrated Python for rendering the table and search functionality
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Transaction History</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
            }}
            .header {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 20px;
            }}
            .search-bar input[type="text"] {{
                padding: 5px;
                font-size: 14px;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }}
            table, th, td {{
                border: 1px solid #ddd;
            }}
            th, td {{
                padding: 10px;
                text-align: left;
            }}
            th {{
                background-color: #f2f2f2;
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <h2>TRANSACTION HISTORY</h2>
            <div class="search-bar">
                <form method="get" action="/">
                    <input type="text" name="search" placeholder="Search by Transaction ID or Client Name" />
                    <button type="submit">Search</button>
                </form>
            </div>
        </div>
        <table>
            <thead>
                <tr>
                    <th>Transaction ID</th>
                    <th>View Payment</th>
                    <th>Client Name</th>
                    <th>Transaction Type</th>
                    <th>Date of Payment</th>
                    <th>Amount Paid</th>
                    <th>Payment Method</th>
                    <th>Payment Status</th>
                </tr>
            </thead>
            <tbody>
                {"".join(f"""
                <tr>
                    <td>{transaction["transaction_id"]}</td>
                    <td><a href="{transaction["view_payment"]}">View</a></td>
                    <td>{transaction["client_name"]}</td>
                    <td>{transaction["transaction_type"]}</td>
                    <td>{transaction["date_of_payment"]}</td>
                    <td>{transaction["amount_paid"]}</td>
                    <td>{transaction["payment_method"]}</td>
                    <td>{transaction["payment_status"]}</td>
                </tr>
                """ for transaction in filtered_transactions)}
            </tbody>
        </table>
    </body>
    </html>
    """

