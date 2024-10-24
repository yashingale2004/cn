import networkx as nx
G = nx.DiGraph()
edges = [
    ('A', 'B', 1),
    ('A', 'C', 4),
    ('B', 'C', 2),
    ('B', 'D', 5),
    ('C', 'D', 1)
]
G.add_weighted_edges_from(edges)
source = 'B'
target = 'D'
shortest_path = nx.dijkstra_path(G, source, target)
shortest_distance = nx.dijkstra_path_length(G, source, target)
print(f"Shortest path from {source} to {target}: {shortest_path}")
print(f"Shortest distance: {shortest_distance}")