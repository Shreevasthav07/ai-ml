graph = {
    'Sibiu': [('Rimnicu Vilcea', 80), ('Fagarus', 99)],
    'Rimnicu Vilcea': [('Pitesti', 97), ('Sibiu', 80)],
    'Pitesti': [('Rimnicu Vilcea', 80), ('Bucharest', 101)],
    'Bucharest': [('Pitesti', 101), ('Fagarus', 211)],
    'Fagarus':[('Sibiu',99),('Bucharest',211)]
}

import heapq
# normal_list --> after appending an elem sort the list --> pop first element for min cost
def uniform_cost_search(graph,start_node,goal_node):
    next_nodes = [(0,start_node,[start_node])]
    visited = {}
    while next_nodes:
        cost, current_node, path = heapq.heappop(next_nodes)
        if current_node == goal_node:
            return cost, path
        if current_node in visited and visited[current_node] <= cost:
            continue
        visited[current_node]= cost
        for neighbor, edgecost in graph.get(current_node,[]):
            updated_cost = cost + edgecost
            updated_path = path + [neighbor]
            heapq.heappush(next_nodes,(updated_cost, neighbor,updated_path))
    return None

result = uniform_cost_search(graph, 'Sibiu', 'Bucharest')
if result is None:
    print("No path found")
else:
    cost, path = result
    print("Cost:", cost)
    print("Path:", path)
    