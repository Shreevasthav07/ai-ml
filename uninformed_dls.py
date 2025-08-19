class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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

if __name__ == "__main__":
    # Creating this binary tree:
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6
    #   / \
    #   7 8 

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    root.left.left.left = Node(7)
    root.left.left.right = Node(8)

    visted_in_dls =dls(root,8,3)
