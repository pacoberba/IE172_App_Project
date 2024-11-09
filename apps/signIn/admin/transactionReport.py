from flask import Flask, render_template_string, request

app = Flask(__name__)

# Placeholder data for total cash inflow and chart
total_inflow = 5000  # Replace with actual data from your database or logic
chart_data = {
    "labels": ["January", "February", "March", "April", "May", "June"],  # Example months
    "data": [1000, 800, 1200, 700, 1300, 1000]  # Example transaction amounts per month
}

@app.route('/transaction-report', methods=['GET', 'POST'])
def transaction_report():
    if request.method == 'POST':
        # Get the form data for the date range (for future filtering or reporting logic)
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        # You can process the selected date range to filter your data if needed
        return f"Transaction Report for Period: {start_date} to {end_date}"

    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Transaction Report Generation</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
            }
            h2 {
                color: #333;
                margin-top: 30px;
            }
            .form-group {
                margin-bottom: 15px;
            }
            input[type="date"] {
                padding: 10px;
                margin: 5px;
                font-size: 16px;
            }
            button {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                cursor: pointer;
                margin-top: 10px;
            }
            button:hover {
                background-color: #45a049;
            }
            .chart-container {
                width: 80%;
                margin-top: 20px;
                display: flex;
                justify-content: center;
            }
        </style>
    </head>
    <body>

        <h2>Transaction Report Generation</h2>

        <p><strong>Total Cash Inflow: </strong>₱{{ total_inflow | round(2) }}</p>

        <!-- Form for selecting date range -->
        <form method="POST">
            <div class="form-group">
                <label for="start_date">Start Date:</label>
                <input type="date" id="start_date" name="start_date" required>
            </div>
            <div class="form-group">
                <label for="end_date">End Date:</label>
                <input type="date" id="end_date" name="end_date" required>
            </div>
            <button type="submit">Generate Report</button>
        </form>

        <!-- Chart Placeholder -->
        <div class="chart-container">
            <canvas id="transactionChart"></canvas>
        </div>

        <script>
            var ctx = document.getElementById('transactionChart').getContext('2d');
            var chartData = {
                labels: {{ chart_data['labels'] | tojson }},
                datasets: [{
                    label: 'Cash Inflow Over Time',
                    data: {{ chart_data['data'] | tojson }},
                    borderColor: 'rgba(75, 192, 192, 1)',
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderWidth: 2
                }]
            };

            var config = {
                type: 'line',
                data: chartData,
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            position: 'top',
                        },
                        tooltip: {
                            mode: 'index',
                            intersect: false,
                        }
                    },
                    scales: {
                        x: {
                            title: {
                                display: true,
                                text: 'Month'
                            }
                        },
                        y: {
                            title: {
                                display: true,
                                text: 'Amount (₱)'
                            },
                            beginAtZero: true
                        }
                    }
                }
            };

            var transactionChart = new Chart(ctx, config);
        </script>

    </body>
    </html>
    """, total_inflow=total_inflow, chart_data=chart_data)


if __name__ == '__main__':
    app.run(debug=True)
