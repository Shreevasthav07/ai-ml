class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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
    # Creating this binary tree:
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    visited_in_ids = ids(root, 6, 1)



    print("Total nodes visited in IDS:", visited_in_ids)
