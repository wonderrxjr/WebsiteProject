from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Render the test.html template
    return render_template('index.html')

@app.route('/media')
def media():
    # Render the media.html template
    return render_template('media.html')

@app.route('/contact')
def contact():
    # Render the contact.html template
    return render_template('contact.html')