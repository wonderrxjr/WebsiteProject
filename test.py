from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Render the test.html template
    return render_template('test.html')