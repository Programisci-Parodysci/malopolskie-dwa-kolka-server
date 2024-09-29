from flask import Flask, request, jsonify
import json
import jwt
import datetime
from functools import wraps
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import os
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'BajoJajo'
bcrypt = Bcrypt(app)
CORS(app)

USER_DATA_FILE = 'users.json'


def extract_gpx_name(gpx_content):
    start_tag = '<name>'
    end_tag = '</name>'

    start_index = gpx_content.find(start_tag) + len(start_tag)
    end_index = gpx_content.find(end_tag)

    if start_index == -1 or end_index == -1:
        return None

    return gpx_content[start_index:end_index].strip()f

def load_user_data():
    if not os.path.exists(USER_DATA_FILE):
        return {}

    with open(USER_DATA_FILE, 'r') as file:
        return json.load(file)


def save_user_data(data):
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data['email']
    password = data['password']

    user_data = load_user_data()

    if email in user_data:
        return jsonify({'message': 'Użytkownik o tej nazwie już istnieje!'}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    user_data[email] = {
        'password': hashed_password,
        'gpx_files': []
    }

    save_user_data(user_data)

    return jsonify({'message': 'Rejestracja zakończona sukcesem!'}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']

    user_data = load_user_data()

    if email not in user_data or not bcrypt.check_password_hash(user_data[email]['password'], password):
        return jsonify({'message': 'Nieprawidłowy login lub hasło!'}), 401

    token = jwt.encode({
        'email': email,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }, app.config['SECRET_KEY'])

    return jsonify({'token': token}), 200


def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token nie został podany!'}), 403

        try:
            token = token.split()[1]
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = data['email']
        except:
            return jsonify({'message': 'Token jest nieprawidłowy lub wygasł!'}), 403

        return f(current_user, *args, **kwargs)

    return wrapper


@app.route('/add_gpx', methods=['POST'])
@token_required
def add_gpx(current_user):
    data = request.get_json()
    gpx_file = data.get('gpx_file')  # Plik GPX jako string

    if not gpx_file:
        return jsonify({'message': 'Brak pliku GPX!'}), 400

    user_data = load_user_data()

    user_data[current_user]['gpx_files'].append(gpx_file)

    save_user_data(user_data)

    return jsonify({'message': 'Plik GPX został dodany!'}), 200


@app.route('/get_gpx_by_name/<gpx_name>', methods=['GET'])
@token_required
def get_gpx_by_name(current_user, gpx_name):
    user_data = load_user_data()
    gpx_files = user_data[current_user]['gpx_files']

    for gpx in gpx_files:
        if extract_gpx_name(gpx) == gpx_name:
            return jsonify({'gpx_file': gpx}), 200

    return jsonify({'message': 'Plik GPX nie został znaleziony!'}), 404





@app.route('/get_gpx', methods=['GET'])
@token_required
def get_gpx(current_user):
    user_data = load_user_data()
    gpx_files = user_data[current_user]['gpx_files']

    return jsonify({'gpx_files': gpx_files}), 200


if __name__ == '__main__':
    if not os.path.exists(USER_DATA_FILE):
        save_user_data({})
    app.run(debug=True)
