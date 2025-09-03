# graph = {
#     'Arad': [('Zerind', 75), ('Timisora', 118)],
#     'Zerind': [('Arad', 75), ('Oradea', 71)],
#     'Oradea': [('Zerind',71), ('Sibiu', 151)],
#     'Sibiu': [('Arad', 140), ('Fagaras',99)],
#     'Fagarus':[('Sibiu',99),('Bucharest',211)],
#     'Bucharest':[('Pitesti',101),('Fagaras',211),('Urziceni',85),('Giurgiu',90)],
#     'Giurgiu':[('Bucharest',90)],
#     'Urzuceni':[('Vaslui',142),('Bucharest',)]
# }

# import heapq
# def a_star(graph,initial_node,goal_node):
#     next_nodes = [(0,initial_node,[initial_node])]
#     visited = set()
#     while next_nodes:
#         cost, current_node, path = heapq.heappop(next_nodes)
#         if current_node == goal_node:
#             return path
#         if current_node in visited:
#             continue
#         visited.add(current_node)
#         for neighbor, heuristic_sld in graph.get(current_node,[]):
#             updated_path = path + [neighbor]
#             heapq.heappush(next_nodes,(heuristic_sld, neighbor,updated_path))
#     return None






# graph = {
#     'Ar': [('T', 118), ('Z', 75), ('S', 140)],
#     'Z': [('Ar', 75), ('O', 71)],
#     'O': [('Z', 71), ('S', 151)],
#     'S': [('Ar', 140), ('F', 99), ('R', 80)],
#     'F': [('S', 99), ('B', 211)],
#     'B': [('F', 211), ('P', 101), ('U', 85), ('G', 90)],
#     'G': [('B', 90)],
#     'U': [('B', 85), ('V', 142), ('H', 98)],
#     'H': [('U', 98), ('E', 86)],
#     'E': [('H', 86)],
#     'V': [('U', 142), ('I', 92)],
#     'I': [('V', 92), ('N', 87)],
#     'N': [('I', 87)],
#     'T': [('Ar', 118), ('L', 111)],
#     'L': [('T', 111), ('M', 70)],
#     'M': [('L', 70), ('D', 75)],
#     'D': [('M', 75), ('C', 120)],
#     'C': [('D', 120), ('R', 146), ('P', 138)],
#     'P': [('C', 138), ('R', 97), ('B', 101)],
#     'R': [('S', 80), ('C', 146), ('P', 97)]
# }

import heapq

graph = {
    'Sibiu': [('Rimnicu Vilcea', 80), ('Fagarus', 99)],
    'Rimnicu Vilcea': [('Pitesti', 97), ('Sibiu', 80)],
    'Pitesti': [('Rimnicu Vilcea', 80), ('Bucharest', 101)],
    'Bucharest': [('Pitesti', 101), ('Fagarus', 211)],
    'Fagarus': [('Sibiu', 99), ('Bucharest', 211)]
}

# Heuristic estimates to goal (Bucharest)
heuristic = {
    'Sibiu': 253,
    'Rimnicu Vilcea': 193,
    'Pitesti': 100,
    'Bucharest': 0,
    'Fagarus': 178
}

def a_star_search(graph, start_node, goal_node, heuristic):
    next_nodes = [(heuristic[start_node], 0, start_node, [start_node])]
    visited = {}

    while next_nodes:
        f_cost, g_cost, current_node, path = heapq.heappop(next_nodes)

        if current_node == goal_node:
            return f_cost,g_cost,path

        if current_node in visited and visited[current_node] <= g_cost:
            continue

        visited[current_node] = g_cost

        for neighbor, edgecost in graph.get(current_node, []):
            new_g = g_cost + edgecost
            new_f = new_g + heuristic.get(neighbor)
            heapq.heappush(next_nodes, (new_f, new_g, neighbor, path + [neighbor]))

    return None

result = a_star_search(graph, 'Sibiu', 'Pitesti',heuristic)
if result is None:
    print("No path found")
else:
    f_cost, g_cost, path = result
    print("Path found:")
    print(" -> ".join(path))
    print(f"Total actual cost (g_cost): {g_cost}")
    print(f"Total estimated cost (f_cost): {f_cost}")



