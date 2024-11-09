from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/schedule-interview', methods=['GET', 'POST'])
def schedule_interview():
    if request.method == 'POST':
        # Handle form submission for selecting an interview date
        interview_date = request.form['interview_date']
        return f"Interview scheduled for {interview_date}."

    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Schedule an Interview</title>
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
                width: 300px;
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
        </style>
    </head>
    <body>

        <h2>Schedule an Interview</h2>

        <form method="POST">
            <div class="form-group">
                <label for="interview_date">Select Interview Date:</label>
                <input type="date" id="interview_date" name="interview_date" required>
            </div>

            <div class="form-group">
                <button type="submit">Schedule Interview</button>
            </div>
        </form>

    </body>
    </html>
    """)

if __name__ == '__main__':
    app.run(debug=True)
