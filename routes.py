import datetime
import os

from flask import render_template, request, send_from_directory

from logic.fizzbuzz import generate_fizzbuzz
from services.media_service import get_media_items


def get_context():
    return {'year': datetime.datetime.now().year}


def register_routes(app):
    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(
            os.path.join(app.root_path, 'static'),
            'favicon.ico',
            mimetype='image/vnd.microsoft.icon',
        )

    @app.route('/')
    @app.route('/index')
    def index():
        return render_template('index.html', **get_context())

    @app.route('/media')
    def media():
        data = get_media_items()
        return render_template('media.html', media=data, **get_context())

    @app.route('/contact')
    def contact():
        return render_template('contact.html', **get_context())

    @app.route('/fizzbuzz', methods=['GET', 'POST'])
    def fizzbuzz():
        results = None
        fizz_value = None
        if request.method == 'POST':
            fizz_value = request.form.get('fizzbuzz')
            results = generate_fizzbuzz(fizz_value)
        return render_template(
            'fizzbuzz.html',
            results=results,
            fizz_value=fizz_value,
            **get_context(),
        )
