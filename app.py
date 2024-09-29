import osmnx as ox
import networkx as nx

from flask import Flask, request, jsonify
import json
import asyncio

import jwt
import datetime
from functools import wraps
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import os


# Define the place and create the graph
app = Flask(__name__)
#secret key?
app.config['SECRET_KEY'] = 'supersekretnyklucz'  # Klucz JWT

bcrypt = Bcrypt(app)
CORS(app)

USER_DATA_FILE = 'users.json'

REPORTS_FILE = 'reports.json'

#map of Cracov:

place_name = "Kraków, Poland"
G = ox.graph_from_place(place_name, network_type="drive")

# Getting the api call for findinf a route from A to B
@app.route('/api', methods = ['GET'])
async def call_route():
    start_latitude  = request.args.get('start_latitude', None)
    start_longitude = request.args.get('start_longitude', None)
    end_latitude  = request.args.get('end_latitude', None)
    end_longitude = request.args.get('end_longitude', None)


    if(not start_latitude or not start_longitude or not end_latitude or not end_longitude):
        return 'WTF U DOIN'

    start_latitude = float(start_latitude)
    start_longitude = float(start_longitude)
    end_latitude = float(end_latitude)
    end_longitude = float(end_longitude)

    # Find the nearest nodes to the coordinates
    start_node = ox.distance.nearest_nodes(G, start_latitude, start_longitude)
    end_node = ox.distance.nearest_nodes(G, end_latitude, end_longitude)

    # Find the shortest path using A* algorithm
    route_nodes = ox.shortest_path(G, start_node, end_node, weight="travel_time")

    #route should be the 'shortest' path.
    route = []

    for node_id in route_nodes:
        node = {}
        node['latitude'] = G.nodes[node_id]['x']
        node['longitude'] = G.nodes[node_id]['y']
        route.append(node)
    json_string = json.dumps(route)
    return json_string

#------------------------------------------------------------

#loading user data:
def load_user_data():
    if not os.path.exists(USER_DATA_FILE):
        return {}

    with open(USER_DATA_FILE, 'r') as file:
        return json.load(file)

#saving user data
def save_user_data(data):
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

 #loading reports
def load_reports():
    if not os.path.exists(REPORTS_FILE):
        return {}

    with open(REPORTS_FILE, 'r') as file:
        return json.load(file)

#saving reports
def save_reports(data):
    with open(REPORTS_FILE, 'w') as file:
        json.dump(data, file, indent=4)


#---------------------

#call to report something on the road
def report_road(u, v, key):
    edge_id = (u, v, key)
    report_data = load_reports()
    if edge_id in report_data:
        report_data[edge_id] += 1
    else:
        report_data[edge_id] = 1
    save_reports(report_data)





@app.route('/report', methods = ['GET'])
async def call_report():
    report_latitude  = request.args.get('report_latitude', None)
    report_longitude = request.args.get('report_longitude', None)

    if(not report_latitude or not report_longitude):
        return 'WTF U DOIN'
    
    report_latitude = float(report_latitude)
    report_longitude = float(report_longitude)

    edge_data = ox.distance.nearest_edges(G, report_latitude, report_longitude)
    # edge_data = G.get_edge_data(u, v, key)
    print(edge_data)


    return 'Report saved!'


#-------------------

#register user
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

#login user
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


@app.route('/get_gpx', methods=['GET'])
@token_required
def get_gpx(current_user):
    user_data = load_user_data()
    gpx_files = user_data[current_user]['gpx_files']

    return jsonify({'gpx_files': gpx_files}), 200


if __name__ == "__main__":
    #app.run(host='0.0.0.0' , port=5000)
    if not os.path.exists(USER_DATA_FILE):
        save_user_data({})
    if not os.path.exists(REPORTS_FILE):
        save_reports({})

    app.run(host='0.0.0.0' , port=40088)