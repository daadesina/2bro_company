from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
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

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/drug')
def drug():
    return render_template('drug.html')

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