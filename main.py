import osmnx as ox
import networkx as nx

# Define the place and create the graph
place_name = "Kraków, Poland"
G = ox.graph_from_place(place_name, network_type="drive")

# Define the coordinates
start_lat, start_lon = 50.06143, 19.93658
end_lat, end_lon = 50.06465, 19.94498

# Find the nearest nodes to the coordinates
start_node = ox.distance.nearest_nodes(G, start_lon, start_lat)
end_node = ox.distance.nearest_nodes(G, end_lon, end_lat)

# Find the shortest path using A* algorithm
route_nodes = ox.shortest_path(G, start_node, end_node, weight="travel_time")
route = []

for node_id in route_nodes:
    node = {}
    node['x'] = G.nodes[node_id]['x']
    node['y'] = G.nodes[node_id]['y']
    route.append(node)


# Print the shortest path
print("Shortest path:", route)