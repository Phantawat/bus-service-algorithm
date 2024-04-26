from collections import defaultdict, deque


def create_graph(data):
    graph = defaultdict(list)
    prev_stop = None

    for stop, line, distance in data:
        if prev_stop is not None:
            if prev_stop != stop:  # Ensure the same stop is not repeated
                graph[prev_stop].append((stop, distance))
        prev_stop = stop

    return graph


def bfs_shortest_route(graph, start, end):
    visited = set()
    queue = deque([(start, [start], 0)])  # Include distance in the queue tuples
    total_distance = 0
    start_passed = False  # Flag to track if the starting point has been passed

    while queue:
        current, path, distance = queue.popleft()
        if start_passed:
            total_distance += distance  # Increment total distance after passing the starting point

        if current == end:
            return path, total_distance  # Return both path and total distance

        if current == start:
            start_passed = True

        visited.add(current)
        for neighbor, dist in graph[current]:
            if neighbor not in visited and neighbor not in path[:-1]:
                queue.append((neighbor, path + [neighbor], dist))

    return None, None


data = [
    ("E1", "1 and 3, special", 0.000), ("E2", "1 and 3", 0.350), ("S1", "1 and 3", 0.250),
    ("C1", "1 and special", 0.150), ("C2", "1", 0.250), ("E12", "1", 0.400), ("E14", "1", 0.300),
    ("C6", "1", 0.200), ("C7", "1", 0.200), ("C8", "1", 0.200), ("W7", "1", 0.300), ("W1", "1", 0.100),
    ("W2", "1", 0.300), ("W3", "1", 0.200), ("C9", "1", 0.200), ("C10", "1", 0.100), ("C11", "1", 0.200),
    ("C12", "1 and special", 0.200), ("E6", "1 and 3", 0.200), ("E5", "1 and 3", 0.200),
    ("E4", "1 and 3", 0.100), ("E3", "1 and 3", 0.100), ("E1 (2)", "1 and 3, special", 0.600)
]

graph = create_graph(data)
print("Available Bus Stops:")
for stop, _, _ in data:
    print(stop)
start = input("Enter where you are: ").capitalize()
end = input("Enter where to go: ").capitalize()

shortest_route, total_distance = bfs_shortest_route(graph, start, end)
print(f"Shortest Route: {shortest_route}")
print(f"Total Distance: {total_distance:.2f} Km.")
