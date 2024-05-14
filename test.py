from flask import Flask, render_template
import mariadb
from dotenv import load_dotenv
import os

load_dotenv()

dbpassword = os.getenv('dbpass')

app = Flask(__name__)
config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'wonderrxjr',
    'password': dbpassword,
    'database': 'website'
}

@app.route('/')
def index():
    # Render the test.html template
    return render_template('index.html')

@app.route('/media')
def media():
    data = []
    try:
        conn = mariadb.connect(**config)
        cur = conn.cursor()
        cur.execute("SELECT * FROM media")
        rows = cur.fetchall()
        for row in rows:
            d = {
                'name': row[1],
                'medium': row[2],
                'platform': row[3],
                'notes': row[4],
            }
            data.append(d)
        print(data)
        conn.close()
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
    # Render the media.html template
    return render_template('media.html', media=data)

@app.route('/contact')
def contact():
    # Render the contact.html template
    return render_template('contact.html')