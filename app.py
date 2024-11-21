from flask import Flask, render_template, request, url_for, redirect
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
    

# @app.route('/create_participant/<caregiver_id>', methods=['GET', 'POST'])
# def create_participant(caregiver_id):
#     if request.method == 'POST':
#         first_names = request.form['first_names']
#         last_names = request.form['last_names']
#         gender = request.form['gender']
#         date_of_birth = request.form['date_of_birth']
#         legal_status = request.form['legal_status']
#         maid_number = request.form['maid_number']
#         ssn = request.form['ssn']
#         phone_number = request.form['phone_number']
#         address_1 = request.form['address_1']
#         address_2 = request.form['address_2']
#         city_state = request.form['city_state']
#         zip_code = request.form['zip_code']

#         # prepare the form data
#         data = {
#             'first_names': first_names,
#             'last_names': last_names,
#             'gender': gender,
#             'date_of_birth': date_of_birth,
#             'legal_status': legal_status,
#             'maid_number': maid_number,
#             'ssn': ssn,
#             'phone_number': phone_number,
#             'address_1': address_1,
#             'address_2': address_2,
#             'city_state': city_state,
#             'zip_code': zip_code,
#         }

#         response = requests.post(
#             f'https://hospital-segment.onrender.com/participant/create/{caregiver_id}', 
#             data=data
#         )

#         if response.status_code == 200:
#             return "Participant created successfully!"
#         else:
#             return "An error occurred."

#     return render_template('profile.html', caregiver_id=caregiver_id)

# @app.route('/create_participant/', methods=['GET', 'POST'])
# def return_home():
#     if request.method == 'POST':
#         return redirect(url_for('home'))
#     return redirect(url_for('home'))

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