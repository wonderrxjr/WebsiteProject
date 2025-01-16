from flask import Flask, render_template, send_from_directory, request
 #import mariadb
from dotenv import load_dotenv
import os
import datetime

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

year = datetime.datetime.now().year

context = {
    'year': year,
}

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route('/')
@app.route('/index')
def index():
    # Render the test.html template
    return render_template('index.html', **context)

# @app.route('/media')
# def media():
#     data = []
#     try:
#         conn = mariadb.connect(**config)
#         cur = conn.cursor()
#         # Will need to be updated to scale in the future
#         cur.execute("SELECT * FROM media")
#         rows = cur.fetchall()
#         for row in rows:
#             d = {
#                 'name': row[1],
#                 'medium': row[2],
#                 'platform': row[3],
#                 'notes': row[4],
#             }
#             data.append(d)
#         print(data)
#         conn.close()
#         def sort_key(d):
#             return d['name']
#         data = sorted(data, key=sort_key)
#     except mariadb.Error as e:
#         print(f"Error connecting to MariaDB Platform: {e}")
#     # Render the media.html template
#     return render_template('media.html', media=data)

@app.route('/contact')
def contact():
    # Render the contact.html template
    return render_template('contact.html', **context)

@app.route('/fizzbuzz', methods =["GET", "POST"])
def fizzbuzz():
    if request.method == "POST":
        print(request.form.get('fizzbuzz'))
        return fizzbuzzhelper(int(request.form.get('fizzbuzz')))
    return render_template('fizzbuzz.html', **context)

def fizzbuzzhelper(n):
    fullout = ""
    for i in range(1, n + 1):
        out = ""
        if i % 3 == 0:
            out += 'Fizz'
        if i % 5 == 0:
            out += 'Buzz'
        if out == '':
            out += str(i)
        fullout = fullout + out + "\n"
    return fullout

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)