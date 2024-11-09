from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/edit-rescue', methods=['GET', 'POST'])
def edit_rescue():
    if request.method == 'POST':
        # Handle form submission for updating the rescue details
        name = request.form['name']
        category = request.form['category']
        gender = request.form['gender']
        age = request.form['age']
        breed = request.form['breed']
        medical_condition = request.form['medical_condition']
        description = request.form['description']
        adopted = 'adopted' in request.form  # If the checkbox is checked, mark as adopted

        # For now, we just print the submitted data (you would save it to a database in a real app)
        return f"Rescue Updated: {name}, {category}, {gender}, {age}, {breed}, {medical_condition}, {description}, Adopted: {adopted}"

    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Edit Rescue Details</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
            }
            h2 {
                color: #333;
                margin-top: 30px;
            }
            input[type="text"], select, textarea {
                padding: 10px;
                margin: 5px;
                width: 300px;
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
            .form-group {
                margin-bottom: 15px;
            }
            .action-buttons {
                display: flex;
                justify-content: space-between;
            }
        </style>
    </head>
    <body>

        <h2>Edit Rescue Details</h2>

        <form method="POST">
            <div class="form-group">
                <label for="name">Rescue Name:</label>
                <input type="text" id="name" name="name" placeholder="Enter rescue name" required>
            </div>

            <div class="form-group">
                <label for="category">Category:</label>
                <select id="category" name="category" required>
                    <option value="Dog">Dog</option>
                    <option value="Cat">Cat</option>
                </select>
            </div>

            <div class="form-group">
                <label for="gender">Gender:</label>
                <select id="gender" name="gender" required>
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                </select>
            </div>

            <div class="form-group">
                <label for="age">Age:</label>
                <input type="text" id="age" name="age" placeholder="Enter age" required>
            </div>

            <div class="form-group">
                <label for="breed">Breed:</label>
                <input type="text" id="breed" name="breed" placeholder="Enter breed" required>
            </div>

            <div class="form-group">
                <label for="medical_condition">Medical Conditions:</label>
                <input type="text" id="medical_condition" name="medical_condition" placeholder="Enter medical conditions" required>
            </div>

            <div class="form-group">
                <label for="description">Description:</label>
                <textarea id="description" name="description" placeholder="Enter description" required></textarea>
            </div>

            <div class="form-group">
                <label for="adopted">Mark as Adopted:</label>
                <input type="checkbox" id="adopted" name="adopted">
            </div>

            <div class="form-group action-buttons">
                <button type="submit">UPDATE</button>
                <button type="button" style="background-color: red;">DELETE</button>
            </div>
        </form>

    </body>
    </html>
    """)

if __name__ == '__main__':
    app.run(debug=True)
