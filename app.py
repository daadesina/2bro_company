from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        """
        Fetch participants from the backend API and render them on profile.html
        """
        BACKEND_PARTICIPANT_API_URL = 'https://hospital-segment.onrender.com/participant/list'

        try:
            response = requests.get(BACKEND_PARTICIPANT_API_URL)
            if response.status_code == 200:
                data = response.json()
                participants = data.get("participants", [])
            else:
                participants = [] # for empty list if the API fails
            return render_template('profile.html', participants=participants)
        except Exception as e:
            return({"status": "error", "message": str(e)}), 500



@app.route('/drug', methods=['GET', 'POST'])
def drug():
    if request.method == 'GET':
        return render_template('drug.html')
    if request.method == 'POST':
        API_URL = 'https://hospital-segment.onrender.com/participant/prescribe'
        # Collect form data and send it to the Flask API
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

        # Add dynamic dose times
        dose = int(request.form.get('dose'))
        for x in range(dose):
            dose_time_key = f"dose_time_{x+1}"
            form_data[dose_time_key] = request.form.get(dose_time_key)

        # Send the data to the API
        response = requests.post(API_URL, data=form_data)
        if response.status_code == 200:
            return redirect(url_for('success'))
        else:
            return render_template('error.html', message=response.json().get('message'))

    return render_template('drug.html')

@app.route('/success')
def success():
    if request.method == 'GET':
        """
        Fetch participants from the backend API and render them on profile.html
        """
        BACKEND_PARTICIPANT_API_URL = 'https://hospital-segment.onrender.com/participant/list'

        try:
            response = requests.get(BACKEND_PARTICIPANT_API_URL)
            if response.status_code == 200:
                data = response.json()
                participants = data.get("participants", [])
            else:
                participants = [] # for empty list if the API fails
            return render_template('response_profile.html', participants=participants)
        except Exception as e:
            return({"status": "error", "message": str(e)}), 500

@app.route('/error')
def error():
    return "An error occurred!"

@app.route('/test')
def test():
    return render_template('_drug.html')


@app.route('/prescription')
def prescription():
    return render_template('prescription.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/caregiver')
def caregiver():
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
        return({"status":"error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)