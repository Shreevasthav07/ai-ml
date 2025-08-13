"""
Goal State:
1 2 3
4 5 6
7 8 0
that is same as [1,2,3,4,5,6,7,8,9,0]
"""

def where_is_blank_space(given_state):
    row_num = (given_state.index(0))//3
    col_num = (given_state.index(0))%3
    return row_num,col_num

def move_up(state):
    blank_space = state.index(0)
    if blank_space >= 3:
        new = state.copy()
        new[blank_space], new[blank_space - 3] = new[blank_space - 3], new[blank_space]
        return new
    return None

def move_down(state):
    blank_space = state.index(0)
    if blank_space <= 5:
        new = state.copy()
        new[blank_space], new[blank_space + 3] = new[blank_space + 3], new[blank_space]
        return new
    return None

def move_left(state):
    blank_space = state.index(0)
    if blank_space % 3 != 0:
        new = state.copy()
        new[blank_space], new[blank_space - 1] = new[blank_space - 1], new[blank_space]
        return new
    return None

def move_right(state):
    blank_space = state.index(0)
    if blank_space % 3 != 2:
        new = state.copy()
        new[blank_space], new[blank_space + 1] = new[blank_space + 1], new[blank_space]
        return new
    return None

def all_possible_states(state):
    next_states = []
    for move in (move_up, move_down, move_left, move_right):
        new_state = move(state)
        if new_state is not None:
            next_states.append(new_state)
    return next_states

def bfs(start_state):
    queue = [start_state]
    visited = {tuple(start_state): None}

    while queue:
        current = queue.pop(0)
        if current == [1,2,3,4,5,6,7,8,0]:
            path = []
            key = tuple(current)
            while key is not None:
                path.append(list(key))
                key = visited[key]
            return path

        for state in all_possible_states(current):
            t = tuple(state)
            if t not in visited:
                visited[t] = tuple(current)
                queue.append(state)

    return None


def dfs(start_state, depth_limit=None):
    stack = [(start_state, None, 0)]
    visited = set()
    parent = {}

    while stack:
        current, par, depth = stack.pop()
        t = tuple(current)
        if t in visited:
            continue
        visited.add(t)
        parent[t] = tuple(par) if par is not None else None

        if current == [1,2,3,4,5,6,7,8,0]:
            path = []
            while t is not None:
                path.append(list(t))
                t = parent[t]
            return path

        if depth_limit is None or depth < depth_limit:
            for next_state in (all_possible_states(current)):
                stack.append((next_state, current, depth + 1))

    return None


if __name__ == "__main__":
    initial = [1, 2, 3, 0, 4,5,6,7,8]
    print("Starting BFS...")
    bfs_solution = bfs(initial)
    if bfs_solution:
        print(f"Solved in {len(bfs_solution) - 1} moves:")
        for step in reversed(bfs_solution):
            print(step)
    else:
        print("No solution found with BFS.")

    print("\nStarting DFS (limit 20)...")
    dfs_solution = dfs(initial, depth_limit=20)
    if dfs_solution:
        print(f"Solved in {len(dfs_solution) - 1} moves:")
        for step in reversed(dfs_solution):
            print(step)
    else:
        print("No solution found within depth limit using DFS.")

