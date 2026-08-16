from flask import Flask
from dotenv import load_dotenv

from routes import register_routes

load_dotenv()

app = Flask(__name__)
register_routes(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)