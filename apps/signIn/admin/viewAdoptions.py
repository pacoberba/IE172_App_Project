from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Placeholder data for rescues
rescues = [
    {
        "rescue_id": "R001",
        "name": "Bella",
        "category": "Dog",
        "gender": "Female",
        "age": "3 years",
        "breed": "Golden Retriever",
        "medical_condition": "Healthy",
        "description": "Friendly and playful",
        "adopted": False
    },
    {
        "rescue_id": "R002",
        "name": "Max",
        "category": "Cat",
        "gender": "Male",
        "age": "2 years",
        "breed": "Persian",
        "medical_condition": "Vaccinated",
        "description": "Calm and affectionate",
        "adopted": False
    }
]

@app.route('/edit-rescue/<rescue_id>', methods=['GET', 'POST'])
def edit_rescue(rescue_id):
    # Find the rescue from the list based on rescue_id
    rescue = next((r for r in rescues if r['rescue_id'] == rescue_id), None)

    if rescue is None:
        return "Rescue not found!", 404

    if request.method == 'POST':
        # Handle form submission for updating the rescue details
        rescue['name'] = request.form['name']
        rescue['category'] = request.form['category']
        rescue['gender'] = request.form['gender']
        rescue['age'] = request.form['age']
        rescue['breed'] = request.form['breed']
        rescue['medical_condition'] = request.form['medical_condition']
        rescue['description'] = request.form['description']
        rescue['adopted'] = 'adopted' in request.form  # If the checkbox is checked, mark as adopted

        # If the delete button is clicked, remove the rescue from the list
        if 'delete' in request.form:
            rescues.remove(rescue)
            return redirect(url_for('rescues_management'))  # Redirect to rescues management page

        # After updating, return to the rescues management page
        return redirect(url_for('rescues_management'))

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
            .delete-button {
                background-color: #f44336;
            }
            .delete-button:hover {
                background-color: #d32f2f;
            }
            .form-group {
                margin-bottom: 15px;
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

            <div class="form-group">
                <label for="upload_file">Upload File:</label>
                <input type="file" id="upload_file" name="upload_file">
            </div>

            <div class="form-group">
                <button type="submit">UPDATE</button>
                <button type="submit" name="delete" class="delete-button">DELETE</button>
            </div>
        </form>

    </body>
    </html>
    """)

@app.route('/rescues-management')
def rescues_management():
    return render_template_string("""
    <h2>Rescues Management</h2>
    <ul>
        {% for rescue in rescues %}
            <li>
                <a href="/edit-rescue/{{ rescue['rescue_id'] }}">Edit Rescue: {{ rescue['name'] }}</a>
            </li>
        {% endfor %}
    </ul>
    """)

