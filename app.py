import osmnx as ox
import networkx as nx

from flask import Flask, request
import json
import asyncio


# Define the place and create the graph
place_name = "Kraków, Poland"
G = ox.graph_from_place(place_name, network_type="drive")

# Getting the api call
@app.route('/api', methods = ['GET'])
async def call():
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


if __name__ == "__main__":
    #app.run(host='0.0.0.0' , port=5000)
    app.run(host='0.0.0.0' , port=40088)