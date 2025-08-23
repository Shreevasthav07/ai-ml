class Graph:
    def __init__(self):
        self.graph={}
    
    def add_vertex(self,v):
        if v not in self.graph:
            self.graph[v]=[]
    
    def add_edge(self,u,v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def show_graph(self):
        for vertex in self.graph:
            print(vertex, "-> ",self.graph[vertex] )

    def dfs(self,root_vertex,goal_vertex):
        if root_vertex not in self.graph or goal_vertex not in self.graph:
            return None
        visited = set()
        parent = {}
        stack=[root_vertex]
        
        while stack:
            vertex = stack.pop()
            if vertex == goal_vertex:
                path = []
                while vertex is not None:
                    path.append(vertex)
                    vertex = parent.get(vertex, None)
                path.reverse()
                return path
            

            if vertex not in visited:
                visited.add(vertex)
                for connected_vertex in self.graph[vertex]:
                    if connected_vertex not in visited:
                        stack.append(connected_vertex)
                        parent[connected_vertex] = vertex
        return None
    
    def bfs(self,root_vertex,goal_vertex):
        if root_vertex not in self.graph or goal_vertex not in self.graph:
            return None
        if root_vertex == goal_vertex:
            return [root_vertex]
        visited = {root_vertex}
        parent = {root_vertex:None}
        queue=[root_vertex]
        
        while queue:
            vertex = queue.pop(0)
            if vertex == goal_vertex:
                path = []
                while vertex is not None:
                    path.append(vertex)
                    vertex = parent.get(vertex, None)
                path.reverse()
                return path
            
            for connected_vertex in self.graph[vertex]:
                if connected_vertex not in visited:
                    visited.add(connected_vertex)
                    queue.append(connected_vertex)
                    parent[connected_vertex] = vertex
        return None
    
    def bidirectional(self,root_vertex, goal_vertex):
        if root_vertex not in self.graph or goal_vertex not in self.graph:
            return None
        q_start = [root_vertex]
        q_goal = [goal_vertex]
        
        
        visited_start = {root_vertex}
        visited_goal = {goal_vertex}
        
        
        parent_start = {root_vertex: None}
        parent_goal = {goal_vertex: None}
        
        while q_start and q_goal:
            if q_start:
                current = q_start.pop(0)
                for neighbor in self.graph[current]:
                    if neighbor not in visited_start:
                        visited_start.add(neighbor)
                        parent_start[neighbor] = current
                        q_start.append(neighbor)
                        
                        if neighbor in visited_goal:
                            return self.construct_path(parent_start, parent_goal, neighbor)
            
            if q_goal:
                current = q_goal.pop(0)
                for neighbor in self.graph[current]:
                    if neighbor not in visited_goal:
                        visited_goal.add(neighbor)
                        parent_goal[neighbor] = current
                        q_goal.append(neighbor)
                        
                        if neighbor in visited_start:
                            return self.construct_path(parent_start, parent_goal, neighbor)
        
        return None 
    
    def construct_path(self, parent_start, parent_goal, meeting_point):
        path_start = []
        node = meeting_point
        while node is not None:
            path_start.append(node)
            node = parent_start.get(node)
        path_start.reverse()

        path_goal = []
        node = parent_goal.get(meeting_point)
        while node is not None:
            path_goal.append(node)
            node = parent_goal.get(node)
        
        return path_start + path_goal

if __name__=="__main__":
    g = Graph()
    n = int(input("Enter number of edges: "))

    for i in range(n):
        u,v= input("Enter edge (u v): ").split(" ")
        g.add_edge(u, v)

    print("\nGraph Representation:")
    g.show_graph()

    node1= input("Enter Starting Point: ")
    node2 = input("Enter Destination Point: ")
    dfs_sol=g.dfs(node1,node2)
    
    if dfs_sol:
        print("DFS Path found:", " -> ".join(dfs_sol))
    else:
        print("No DFS path exists between", node1, "and", node2)
    
    bfs_sol=g.bfs(node1,node2)
    
    if bfs_sol:
        print("BFS Path found:", " -> ".join(bfs_sol))
    else:
        print("No BFS path exists between", node1, "and", node2)

    path = g.bidirectional(node1,node2)
    if path:
        print("Bidirectional Search Path:", " -> ".join(path))
    else:
        print("No path exists between", node1, "and", node2)

    