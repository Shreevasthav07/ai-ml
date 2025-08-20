class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def bfs(root,search):
    if root is None:
        return
    queue = [root]
    found = None
    bfs_counter = 0
    print("BFS Traversal:", end=" ")
    
    while (found==None and queue):
        node = queue.pop(0)
        bfs_counter+=1
        print(node.value, end=" ")
        if node.value == search:
            found = node.value
            print("\nFound Element")
            return bfs_counter
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    if found ==None:
        print("\nElement Not Found")
        return bfs_counter
    


def dfs(root,search):
    if root is None:
        return
    stack = [root]
    found = None
    dfs_counter = 0

    print("DFS Traversal:", end=" ")
    while (found ==None and stack):
        node = stack.pop()
        dfs_counter+=1
        print(node.value, end=" ")
        if node.value == search:
            found = node.value
            print("\nFound Element")
            return dfs_counter
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    if found ==None:
        print("\nElement Not Found")
        return dfs_counter
    print()

def dls(root, search, limit):
    if root is None:
        return None
    stack = [(root, 0)]
    dfs_counter = 0

    print(f"DLS Traversal (limit={limit}):", end=" ")
    while stack:
        node, depth = stack.pop()
        dfs_counter += 1
        print(node.value, end=" ")

        if node.value == search:
            print("\nFound Element")
            return dfs_counter
        
        if depth < limit:
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))

    print("\nElement Not Found within depth limit")
    return dfs_counter

def ids(root, search, max_depth):
    total_visited = 0
    print(f"IDS Traversal up to depth {max_depth}:")
    
    for limit in range(max_depth + 1):
        print(f"  Depth {limit}: ", end="")
        stack = [(root, 0)]
        visited_this_depth = 0
        found = False

        while stack:
            node, depth = stack.pop()
            visited_this_depth += 1
            print(node.value, end=" ")

            if node.value == search:
                print("\nFound Element at depth", limit)
                total_visited += visited_this_depth
                return total_visited

            if depth < limit:
                if node.right:
                    stack.append((node.right, depth + 1))
                if node.left:
                    stack.append((node.left, depth + 1))

        total_visited += visited_this_depth
        print()

    print("\nElement Not Found within depth limit")
    return total_visited

if __name__ == "__main__":

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    visted_in_bfs=bfs(root,3)
    print()
    visited_in_dfs=dfs(root,3)
    print()
    visted_in_dls =dls(root,6,2)
    print()
    visited_in_ids = ids(root, 6, 2)
    print()
    print(f"number of nodes visited in bfs:{visted_in_bfs}")
    print(f"number of nodes visited in dfs:{visited_in_dfs}")
    print(f"number of nodes visited in dls:{visted_in_dls}")
    print(f"number of nodes visited in ids:{visited_in_ids}")
