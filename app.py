from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

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

@app.route('/indexZ')
def indexZ ():
    return render_template('indexZ.html')

@app.route('/create')
def create ():
    return render_template('create_participant.html')

if __name__ == '__main__':
    app.run(debug=True)