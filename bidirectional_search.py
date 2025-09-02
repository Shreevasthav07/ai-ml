graph = {
    'Sibiu':['Fagaras', 'Rimnicu Vilcea'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Rimnicu Vilcea': ['Sibiu', 'Pitesti'],
    'Pitesti':['Rimnicu Vilcea','Bucharest'],
    'Bucharest':['Pitesti','Fagaras']
}
def bidirectional_search(initial,goal,graph):
    if initial == goal:
        return [initial]
    queue_from_initial = [initial]
    queue_from_goal = [goal]
    visited_from_initial = {initial: None}
    visited_from_goal = {goal: None}

    while queue_from_initial and queue_from_goal:
        if queue_from_initial:
            current = queue_from_initial.pop(0)
            for neighbor in graph[current]:
                if neighbor not in visited_from_initial:
                    visited_from_initial[neighbor] = current
                    queue_from_initial.append(neighbor)
                    
                    
                    if neighbor in visited_from_goal:
                        forward_path, backward_path = build_path(visited_from_initial, visited_from_goal, neighbor)
                        return forward_path, backward_path
        
       
        if queue_from_goal:
            current = queue_from_goal.pop(0)
            for neighbor in graph[current]:
                if neighbor not in visited_from_goal:
                    visited_from_goal[neighbor] = current
                    queue_from_goal.append(neighbor)
                    
                    if neighbor in visited_from_initial:
                        return build_path(visited_from_initial, visited_from_goal, neighbor)
    
    return None

def build_path(forward_visited, backward_visited, meeting_point):

    path1 = []
    node = meeting_point
    while node is not None:
        path1.append(node)
        node = forward_visited[node]
    path1.reverse()
    
    
    path2 = []
    node = meeting_point
    while node is not None:
        path2.append(node)
        node = backward_visited[node]
    
    return path1, path2



graph2 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
result = bidirectional_search('A', 'E', graph2)
print("Forward Path:", result[0])
print("Backward Path:", result[1])
print("Full Path:", result[0] + result[1][1:])