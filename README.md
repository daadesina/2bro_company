# Hospital Web Application Frontend

This repository contains the frontend of a hospital management system built with Python Flask. The application interfaces with a backend API to handle participant management, caregiver details, drug prescriptions, and other hospital-related functionalities.

## Features

- **Participant Management**: View, create, and manage participants.
- **Caregiver Details**: Retrieve and display details of caregivers.
- **Drug Prescription**: Handle drug prescription processes.
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

   - git clone https://github.com/daadesina/2bro_company.git
   - cd 2bro_company

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

<p>project/</p>
<p>│</p>
<p>├── static/               # Contains static files</p>
<p>│   ├── css/              # CSS files</p>
<p>│   ├── js/               # JavaScript files</p>
<p>│   ├── images/           # Images and icons</p>
<p>│</p>
<p>├── templates/            # HTML templates</p>
<p>│   ├── home.html         # Parent template</p>
<p>│   ├── profile.html      # Participant profile page</p>
<p>│   ├── drug.html         # Drug prescription form</p>
<p>│   ├── caregiver.html    # Caregiver details</p>
<p>│   ├── error.html        # Error page</p>
<p>│   ├── settings.html     # Settings page</p>
<p>|   ├── prescription.html #Prescription page</p>
<p>│</p>
<p>├── app.py                # Main Flask application logic</p>
<p>├── requirements.txt      # Python dependencies</p>
<p>├── README.md             # Project documentation</p>

## Routes

<table>
    <thead>
        <th>Route</th>
        <th>Methods</th>
        <th>Description</th>
    </thead>
    <tbody>
        <tr>
            <td>/</td>
            <td>GET, POST</td>
            <td>Displays the list of participants fetched from the backend API.</td>
        </tr>
        <tr>
            <td>/create_participant</td>
            <td>POST</td>
            <td>Form to create a new participant.</td>
        </tr>
        <tr>
            <td>/drug</td>
            <td>GET, POST</td>
            <td>Form to manage drug prescriptions.</td>
        </tr>
        <tr>
            <td>/success</td>
            <td>GET</td>
            <td>Displays a success message after an action is completed.</td>
        </tr>
        <tr>
            <td>/error</td>
            <td>GET</td>
            <td>Displays a generic error message.</td>
        </tr>
        <tr>
            <td>/prescription</td>
            <td>GET</td>
            <td>Displays the prescription template.</td>
        </tr>
        <tr>
            <td>/settings</td>
            <td>GET</td>
            <td>Displays the settings page.</td>
        </tr>
        <tr>
            <td>/caregiver</td>
            <td>GET</td>
            <td>Fetches and displays caregiver details from the backend API.</td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
        </tr>
    </tbody>
</table>