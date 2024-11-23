from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS
import requests

# Initialize Flask application
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS) for the app
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Fetch participants from the backend API and render them on the profile page.

    Methods:
        GET: Fetches a list of participants from the backend API and passes it to the profile.html template.
        POST: Not specifically handled but included for compatibility.
    
    Returns:
        Renders the profile.html template with a list of participants or an error message in case of failure.
    """
    BACKEND_PARTICIPANT_API_URL = 'https://hospital-segment.onrender.com/participant/list'

    try:
        response = requests.get(BACKEND_PARTICIPANT_API_URL)
        if response.status_code == 200:
            data = response.json()
            participants = data.get("participants", [])
        else:
            participants = []  # Fallback in case the API fails
        return render_template('profile.html', participants=participants)
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/create_participant', methods=['POST'])
def create_participant():
    """
    Handles creating a new participant by sending form data to the backend API.

    Methods:
        POST: Collects form data from the request and sends it to the backend API for participant creation.
    
    Returns:
        Redirects to the home page upon success or renders an error page with the API's error message.
    """
    BACKEND_PARTICIPANT_API = 'https://hospital-segment.onrender.com/participant/create'

    if request.method == 'POST':
        form_data = {
            "caregiver": request.form.get('caregiver_id'),
            "first_names": request.form.get('first_names'),
            "middle_name_initial": request.form.get("middle_name_initial"),
            "last_names": request.form.get('last_names'),
            "gender": request.form.get('gender'),
            "date_of_birth": request.form.get('date_of_birth'),
            "legal_status": request.form.get('legal_status'),
            "maid_number": request.form.get('maid_number'),
            "ssn": request.form.get('ssn'),
            "phone_number": request.form.get('phone_number'),
            "address_1": request.form.get('address_1'),
            "address_2": request.form.get('address_2'),
            "city_state": request.form.get('city_state'),
            "zip_code": request.form.get('zip_code')
        }

        response = requests.post(BACKEND_PARTICIPANT_API, data=form_data)
        if response.status_code == 200:
            return redirect(url_for('home'))
        else:
            return render_template('error.html', message=response.json().get('message'))

    return render_template('home.html')

@app.route('/drug', methods=['GET', 'POST'])
def drug():
    """
    Handles drug prescription management.

    Methods:
        GET: Renders the drug.html template.
        POST: Sends form data to the backend API to prescribe medication to a participant.
    
    Returns:
        Redirects to a success page upon success or renders an error page in case of failure.
    """
    if request.method == 'GET':
        return render_template('drug.html')
    if request.method == 'POST':
        API_URL = 'https://hospital-segment.onrender.com/participant/prescribe'

        form_data = {
            "caregiver_id": request.form.get('caregiver_id'),
            "participant_id": request.form.get('participant_id'),
            "drug_id": request.form.get('drug_id'),
            "reason_for_medication": request.form.get('reason_for_medication'),
            "prescriber": request.form.get('prescriber'),
            "pharmacy_id": request.form.get('pharmacy_id'),
            "quantity_dosage": request.form.get('quantity_dosage'),
            "refills": request.form.get('refills'),
            "start_date": request.form.get('start_date'),
            "dose": request.form.get('dose'),
            "frequency": request.form.get('frequency'),
            "comment": request.form.get('comment'),
        }

        # Add dynamic dose times based on the dose count
        dose = int(request.form.get('dose'))
        for x in range(dose):
            dose_time_key = f"dose_time_{x+1}"
            form_data[dose_time_key] = request.form.get(dose_time_key)

        response = requests.post(API_URL, data=form_data)
        if response.status_code == 200:
            return redirect(url_for('success'))
        else:
            return render_template('error.html', message=response.json().get('message'))

    return render_template('drug.html')

@app.route('/success')
def success():
    """
    Displays a success page with a list of participants.

    Methods:
        GET: Fetches participant data and renders it on the response_profile.html template.
    
    Returns:
        Renders the response_profile.html template with participant data or an error message in case of failure.
    """
    BACKEND_PARTICIPANT_API_URL = 'https://hospital-segment.onrender.com/participant/list'

    try:
        response = requests.get(BACKEND_PARTICIPANT_API_URL)
        if response.status_code == 200:
            data = response.json()
            participants = data.get("participants", [])
        else:
            participants = []
        return render_template('response_profile.html', participants=participants)
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/error')
def error():
    """
    Displays a generic error message.
    """
    return "An error occurred!"

@app.route('/prescription')
def prescription():
    """
    Renders the prescription.html template.
    """
    return render_template('prescription.html')

@app.route('/settings')
def settings():
    """
    Renders the settings.html template.
    """
    return render_template('settings.html')

@app.route('/caregiver')
def caregiver():
    """
    Fetches caregiver details from the backend API and renders them on the caregiver.html template.

    Returns:
        Renders the caregiver.html template with caregiver details or an error message in case of failure.
    """
    BACKEND_CAREGIVER_API_URL = 'https://hospital-segment.onrender.com/caregiver/details'

    try:
        response = requests.get(BACKEND_CAREGIVER_API_URL)
        if response.status_code == 200:
            data = response.json()
            caregivers = data.get("caregiver_details", [])
        else:
            caregivers = []
        return render_template('caregiver.html', caregivers=caregivers)
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Entry point for the Flask application
if __name__ == '__main__':
    app.run(debug=True)
