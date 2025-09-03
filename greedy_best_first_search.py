import heapq

def greedy_best_first_search(graph,initial_node,goal_node):
    next_nodes = [(0,initial_node,[initial_node])]
    visited = set()
    while next_nodes:
        cost, current_node, path = heapq.heappop(next_nodes)
        if current_node == goal_node:
            return path
        if current_node in visited:
            continue
        visited.add(current_node)
        for neighbor, heuristic_sld in graph.get(current_node,[]):
            updated_path = path + [neighbor]
            heapq.heappush(next_nodes,(heuristic_sld, neighbor,updated_path))
    return None

graph_with_heuristic = {
    'Ar': [('T', 329), ('Z', 374), ('S', 253)],
    'Z': [('Ar', 366), ('O', 380)],
    'O': [('Z', 374), ('S', 253)],
    'S': [('Ar', 366), ('F', 176), ('R', 193)],
    'F': [('S', 253), ('B', 0)],
    'B': [('F', 176), ('P', 100), ('U', 80), ('G', 77)],
    'G': [('B', 0)],
    'U': [('B', 0), ('V', 199), ('H', 151)],
    'H': [('U', 80), ('E', 161)],
    'E': [('H', 151)],
    'V': [('U', 80), ('I', 226)],
    'I': [('V', 199), ('N', 234)],
    'N': [('I', 226)],
    'T': [('Ar', 366), ('L', 244)],
    'L': [('T', 329), ('M', 241)],
    'M': [('L', 244), ('D', 242)],
    'D': [('M', 241), ('C', 160)],
    'C': [('D', 242), ('R', 193), ('P', 100)],
    'P': [('C', 160), ('R', 193), ('B', 0)],
    'R': [('S', 253), ('C', 160), ('P', 100)]
}

result = greedy_best_first_search(graph_with_heuristic, 'Ar', 'B')
if result is None:
    print("No path found")
else:
    print("Path:", result)























