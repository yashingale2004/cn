import heapq

# Function to calculate the shortest path using Dijkstra's algorithm
def dijkstra(graph, start, target):
    # Priority queue to store the minimum distance to a node
    queue = [(0, start)]  # (distance, node)
    distances = {node: float('infinity') for node in graph}  # Initially, all distances are infinity
    distances[start] = 0  # Distance to the start node is 0
    previous_nodes = {node: None for node in graph}  # To store the previous node for each node
    visited = set()  # Set to track visited nodes
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if current_node in visited:
            continue
        visited.add(current_node)
        
        # If we reach the target node, reconstruct the path
        if current_node == target:
            path = []
            while current_node:
                path.insert(0, current_node)
                current_node = previous_nodes[current_node]
            return distances[target], path
        
        # Loop through the neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))
    
    return float('infinity'), []  # If the target is unreachable

# Predefined graph based on your input
def create_graph():
    graph = {
        '1': {'2': 3, '4': 4, '3': 24},
        '2': {'1': 3, '3': 6, '4': 9},
        '3': {'2': 6, '4': 20, '1': 24},
        '4': {'3': 20, '1': 4, '2': 9}
    }
    return graph

if __name__ == "__main__":
    graph = create_graph()
    start_router = '1'  # Starting router
    target_router = '3'  # Target router
    
    # Find the shortest path from the start router to the target router
    shortest_path_distance, path = dijkstra(graph, start_router, target_router)
    
    if path:
        # Display the shortest path distance and the route
        print(f"\nShortest path from router {start_router} to router {target_router}: {shortest_path_distance}")
        print(f"Route: {' -> '.join(path)}")
    else:
        print(f"No path found from router {start_router} to router {target_router}")