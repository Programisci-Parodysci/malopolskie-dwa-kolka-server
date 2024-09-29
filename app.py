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
from src.func import get_suggestions_photon, get_coordinates_from_address, get_readable_adresses


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
G_bike = ox.graph_from_place(place_name, network_type="bike")
G_all = ox.graph_from_place(place_name, network_type="all")

G_all = ox.add_edge_speeds(G_all)
#get ids of nodes with bike roads between them:

bike_coords = []

for u, v, key, data in G_bike.edges(keys=True, data=True):
    node1 = G_bike.nodes[u]
    node2 = G_bike.nodes[v]

    bike_coords.append((u, v))




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
    start_node = ox.distance.nearest_nodes(G_bike, start_latitude, start_longitude)
    end_node = ox.distance.nearest_nodes(G_bike, end_latitude, end_longitude)

    # Find the shortest path using A* algorithm
    route_nodes = ox.shortest_path(G_bike, start_node, end_node, weight="travel_time")

    #route should be the 'shortest' path.
    route = []

    for node_id in route_nodes:
        node = {}
        node['latitude'] = G_bike.nodes[node_id]['x']
        node['longitude'] = G_bike.nodes[node_id]['y']
        route.append(node)
    json_string = json.dumps(route)
    return json_string


# safe route from A to B
@app.route('/safe_route', methods = ['GET'])
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
    start_node = ox.distance.nearest_nodes(G_all, start_latitude, start_longitude)
    end_node = ox.distance.nearest_nodes(G_all, end_latitude, end_longitude)

    # Find the shortest path using A* algorithm
    route_nodes = ox.shortest_path(G_all, start_node, end_node, weight="danger_score")

    #route should be the 'shortest' path.
    route = []

    for node_id in route_nodes:
        node = {}
        node['latitude'] = G_bike.nodes[node_id]['x']
        node['longitude'] = G_bike.nodes[node_id]['y']
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
        print(file)
        return json.load(file)

#saving reports
def save_reports(data):
    with open(REPORTS_FILE, 'w') as file:
        json.dump(data, file, indent=4)


#---------------------

#call to report something on the road
def report_road(u, v, key):
    edge_id = f"{u},{v},{key}"
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

    u, v, key = ox.distance.nearest_edges(G_bike, report_latitude, report_longitude)
    # edge_data = G.get_edge_data(u, v, key)
    report_road(u, v, key)

    return 'Report saved!'

@app.route('/get_sugg', methods = ['GET'])
async def call_sugg():
    letters = request.args.get('letters', None)

    if(not letters):
        return 'WTF U DOIN'

    content = get_readable_adresses(5,get_suggestions_photon(letters+', Lesser Poland Voivodeship'))
    return content

@app.route('/get_coords', methods = ['GET'])
async def call_coords():
    address = request.args.get('address', None)

    if(not address):
        return 'WTF U DOIN'

    coords = get_coordinates_from_address(address)
    return coords


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


def calculate_danger():

    for u, v, data in G_all.edges(data=True):
        street_count_u = G_all.nodes[u]['street_count']
        street_count_v = G_all.nodes[v]['street_count']


        data['avg_intersection_num'] = (street_count_u + street_count_v) / 2

        avg_intersection_num = data['avg_intersection_num']

        if avg_intersection_num >= 3.5:
            data['intersection_score'] = 0.5
        elif avg_intersection_num < 3.5:
            data['intersection_score'] = 0.5

        # Speed score [0, 1]
        speed = data['speed_kph']
        if 80 < speed:
            data['speed_score'] = 1
        elif 50 < speed <= 80:
            data['speed_score'] = 0.75
        elif 35 < speed <= 50:
            data['speed_score'] = 0.5
        elif 25 <= speed <= 35:
            data['speed_score'] = 0.25
        elif speed < 25:
            data['speed_score'] = 0

        if (u, v) in bike_coords:
            data['bike_score'] = 0
        else:
            data['bike_score'] = 1


    # Create danger score (intersections score not used for now)
    data['danger_score'] = data['speed_score'] + data['bike_score']




if __name__ == "__main__":
    #app.run(host='0.0.0.0' , port=5000)
    if not os.path.exists(USER_DATA_FILE):
        save_user_data({})
    if not os.path.exists(REPORTS_FILE):
        save_reports({})
    calculate_danger()

    app.run(host='0.0.0.0' , port=40088)