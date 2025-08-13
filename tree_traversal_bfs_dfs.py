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

    visted_in_bfs =bfs(root,3)
    visited_in_dfs=dfs(root,3)

    if visted_in_bfs< visited_in_dfs:
        print("Time taken for BFS is less than that of DFS")
    elif visted_in_bfs == visited_in_dfs:
        print("Time taken for  BFS and DFS are Equal")
    else:
        print("Time taken for  BFS is more than DFS")
