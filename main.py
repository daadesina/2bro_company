from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests

app = Flask(__name__)

# Replace with the actual URL of your backend API
API_URL = 'https://hospital-segment.onrender.com/participant/prescribe'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prescribe', methods=['GET', 'POST'])
def prescribe():
    if request.method == 'POST':
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
    return "Prescription created successfully!"

@app.route('/error')
def error():
    return "An error occurred!"

if __name__ == '__main__':
    app.run(debug=True)
