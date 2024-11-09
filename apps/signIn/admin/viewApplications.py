from flask import Flask

app = Flask(__name__)

@app.route('/view-application/<application_number>')
def view_application(application_number):
    # Placeholder data for the application details
    adopter_info = {
        "last_name": "Rizal",
        "first_name": "Jose",
        "middle_name": "A.",
        "suffix": "Jr.",
        "street_address": "1234 QC St",
        "barangay": "Barangay 1",
        "city_municipality": "Metro City",
        "province": "Metro Province",
        "contact_number": "123-456-7890",
        "email_address": "jrizzler@example.com",
        "facebook_link": "https://facebook.com/jrizz",
        "instagram_link": "https://instagram.com/jrizz",
        "birthdate": "1990-01-01",
        "source_of_income": "Employed",
        "type_of_dwelling": "Apartment",
        "dwelling_ownership": "Rented",
        "are_pets_allowed": "Yes",
        "pet_name": "Buddy",
        "pet_gender": "Male",
        "pet_age": "2 years",
        "pet_breed": "Mixed",
        "pet_medical_condition": "Healthy",
        "pet_description": "Friendly and playful",
        "preliminary_motivation": "Loves animals, responsible caregiver",
        "reason_for_fostering": "To provide a safe temporary home",
        "has_experience": "Yes",
        "willing_medical_expenses": "Yes",
        "aware_and_agree_fee": "Yes",
        "number_of_members": "4",
        "supportive_members": "Yes",
        "planning_to_move": "No",
        "responsible_for_pet_care": "Jose Rizal",
        "pet_as_gift": "No",
        "ownership_experience": "Owned 2 pets",
        "vet_clinic": "PetCare Clinic",
        "past_pets": "Dog, Cat",
        "still_own_all": "No, passed away",
        "how_did_you_find_us": "Social Media",
        "why_consider_adopting": "Wants to give a loving home",
        "copy_of_id": "Provided",
        "available_times": "Weekdays after 6 PM"
    }

    # HTML code with integrated Python for displaying the information
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>View Application: {application_number}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
            }}
            h2 {{
                color: #333;
                margin-top: 30px;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 10px;
            }}
            th, td {{
                padding: 10px;
                text-align: left;
                border: 1px solid #ddd;
                width: 50%;
            }}
            th {{
                background-color: #f2f2f2;
            }}
        </style>
    </head>
    <body>
        <h2>VIEW APPLICATION: {application_number}</h2>

        <h3>Adopter Personal Information</h3>
        <table>
            <tr><th>Last Name</th><td>{adopter_info["last_name"]}</td></tr>
            <tr><th>First Name</th><td>{adopter_info["first_name"]}</td></tr>
            <tr><th>Middle Name</th><td>{adopter_info["middle_name"]}</td></tr>
            <tr><th>Suffix</th><td>{adopter_info["suffix"]}</td></tr>
        </table>

        <table>
            <tr><th>Street Address</th><td>{adopter_info["street_address"]}</td></tr>
            <tr><th>Barangay</th><td>{adopter_info["barangay"]}</td></tr>
            <tr><th>City/Municipality</th><td>{adopter_info["city_municipality"]}</td></tr>
            <tr><th>Province</th><td>{adopter_info["province"]}</td></tr>
        </table>

        <table>
            <tr><th>Contact Number</th><td>{adopter_info["contact_number"]}</td></tr>
            <tr><th>Email Address</th><td>{adopter_info["email_address"]}</td></tr>
            <tr><th>Facebook Link</th><td>{adopter_info["facebook_link"]}</td></tr>
            <tr><th>Instagram Link</th><td>{adopter_info["instagram_link"]}</td></tr>
        </table>

        <table>
            <tr><th>Birthdate</th><td>{adopter_info["birthdate"]}</td></tr>
            <tr><th>Source of Income</th><td>{adopter_info["source_of_income"]}</td></tr>
        </table>

        <h3>Adopter Dwelling Information</h3>
        <table>
            <tr><th>Type of Dwelling</th><td>{adopter_info["type_of_dwelling"]}</td></tr>
            <tr><th>Dwelling Ownership</th><td>{adopter_info["dwelling_ownership"]}</td></tr>
            <tr><th>Are Pets Allowed?</th><td>{adopter_info["are_pets_allowed"]}</td></tr>
        </table>

        <h3>Chosen Pet Information</h3>
        <table>
            <tr><th>Name</th><td>{adopter_info["pet_name"]}</td></tr>
            <tr><th>Gender</th><td>{adopter_info["pet_gender"]}</td></tr>
            <tr><th>Age</th><td>{adopter_info["pet_age"]}</td></tr>
            <tr><th>Breed</th><td>{adopter_info["pet_breed"]}</td></tr>
            <tr><th>Medical Condition</th><td>{adopter_info["pet_medical_condition"]}</td></tr>
            <tr><th>Description</th><td>{adopter_info["pet_description"]}</td></tr>
        </table>

        <h3>Preliminary Motivation</h3>
        <table>
            <tr><th>Best Description of Adopter</th><td>{adopter_info["preliminary_motivation"]}</td></tr>
        </table>

        <h3>Passion Project Foster Volunteer</h3>
        <table>
            <tr><th>Reason for Fostering</th><td>{adopter_info["reason_for_fostering"]}</td></tr>
            <tr><th>Has Experience</th><td>{adopter_info["has_experience"]}</td></tr>
            <tr><th>Willing to Shoulder Medical Expenses</th><td>{adopter_info["willing_medical_expenses"]}</td></tr>
        </table>

        <h3>Notice on Adoption Fee</h3>
        <table>
            <tr><th>Aware and Agree</th><td>{adopter_info["aware_and_agree_fee"]}</td></tr>
        </table>

        <h3>Household Information</h3>
        <table>
            <tr><th>Number of Members</th><td>{adopter_info["number_of_members"]}</td></tr>
            <tr><th>All Members Supportive of Adopting</th><td>{adopter_info["supportive_members"]}</td></tr>
            <tr><th>Planning to Move</th><td>{adopter_info["planning_to_move"]}</td></tr>
        </table>

        <h3>Adoption and Pet Care Information</h3>
        <table>
            <tr><th>Who is Responsible for Pet Care?</th><td>{adopter_info["responsible_for_pet_care"]}</td></tr>
            <tr><th>Pet as a Gift?</th><td>{adopter_info["pet_as_gift"]}</td></tr>
            <tr><th>Ownership Experience</th><td>{adopter_info["ownership_experience"]}</td></tr>
            <tr><th>Vet Clinic</th><td>{adopter_info["vet_clinic"]}</td></tr>
            <tr><th>All Pets Owned in the Past 5 Years</th><td>{adopter_info["past_pets"]}</td></tr>
            <tr><th>Still Own All? If Not, What Happened?</th><td>{adopter_info["still_own_all"]}</td></tr>
        </table>

        <h3>Other Information</h3>
        <table>
            <tr><th>How Did You Find Out About Passion Project and the Adoption Program?</th><td>{adopter_info["how_did_you_find_us"]}</td></tr>
            <tr><th>What Made You Consider Adopting?</th><td>{adopter_info["why_consider_adopting"]}</td></tr>
            <tr><th>Copy of Valid ID</th><td>{adopter_info["copy_of_id"]}</td></tr>
            <tr><th>Available Times for Adoption Interview</th><td>{adopter_info["available_times"]}</td></tr>
        </table>

    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
