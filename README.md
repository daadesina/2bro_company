# Hospital Web Application Frontend

This repository contains the frontend of a hospital management system built with Python Flask. The application interfaces with a backend API to handle participant management, caregiver details, drug prescriptions, and other hospital-related functionalities.

## Features

- **Participant Management**: View, create, and manage participants.
- **Caregiver Details**: Retrieve and display details of caregivers.
- **Drug Prescription**: Handle drug prescription processes.
- **Settings**: Configurable application settings.
- **Dynamic Routing**: Routes for each functional module.
- **Error Handling**: Custom error pages for better user experience.

---

## Table of Contents

1. [Tech Stack](#tech-stack)
2. [Setup](#setup)
3. [Project Structure](#project-structure)
4. [Routes](#routes)

---

## Tech Stack

- **Frontend Framework**: Python Flask
- **Styling**: Tailwind CSS and custom CSS
- **Backend API**: [Hospital Segment API](https://hospital-segment.onrender.com)
- **Other Dependencies**: Flask-CORS, Requests

---

## Setup

### Prerequisites

Ensure you have the following installed:

- Python 3.1 or higher
- Flask
- pip (Python package installer)

### Installation Steps

1. **Clone the repository**:

   git clone https://github.com/daadesina/2bro_company.git
   cd 2bro_company

2. **Create a virtual environment:**

    python -m venv flaskenv
    flaskenv\Scripts\activate

3. **Install dependencies:**

    pip install -r requirements.txt

4. **Run the application:**

    python app.py

5. **Access the app:**

    Open your browser and navigate to http://127.0.0.1:5000

## Project Structure

project/
│
├── static/               # Contains static files
│   ├── css/              # CSS files
│   ├── js/               # JavaScript files
│   ├── images/           # Images and icons
│
├── templates/            # HTML templates
│   ├── home.html         # Parent template
│   ├── profile.html      # Participant profile page
│   ├── drug.html         # Drug prescription form
│   ├── caregiver.html    # Caregiver details
│   ├── error.html        # Error page
│   ├── settings.html     # Settings page
|   ├── prescription.html #Prescription page
│
├── app.py                # Main Flask application logic
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation

## Routes


Route	                    Methods	            Description
---------------------------------------------------------------------------------------------------------------------
/	                        GET, POST	        Displays the list of participants fetched from the backend API.
/create_participant	          POST	            Form to create a new participant.
/drug	                    GET, POST	        Form to manage drug prescriptions.
/success	                   GET	            Displays a success message after an action is completed.
/error	                       GET	            Displays a generic error message.
/prescription	               GET	            Displays the prescription template.
/settings	                   GET	            Displays the settings page.
/caregiver	                   GET	            Fetches and displays caregiver details from the backend API.
