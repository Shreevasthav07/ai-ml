"""
goal state:
[],[],[3,2,1]
"""
stick1 = [3,2,1]
stick2=[]
stick3 = []
state = [stick1,stick2,stick3]

goal_state = [[],[],[3,2,1]]

def rough_copy(state):
    new_state=[]
    for stick in state:
        new_state.append(stick.copy())
    return new_state

def from_stick1_to_stick2(state):
    new_state = rough_copy(state)
    if new_state[0]:
        if new_state[1] == [] or new_state[1][-1] > new_state[0][-1]:
            ring = new_state[0].pop()
            new_state[1].append(ring)
            return new_state
    return None

def from_stick1_to_stick3(state):
    new_state = rough_copy(state)
    if new_state[0]:
        if new_state[2] == [] or new_state[2][-1] > new_state[0][-1]:
            ring = new_state[0].pop()
            new_state[2].append(ring)
            return new_state
    return None

def from_stick2_to_stick1(state):
    new_state = rough_copy(state)
    if new_state[1]:
        if new_state[0] == [] or new_state[0][-1] > new_state[1][-1]:
            ring = new_state[1].pop()
            new_state[0].append(ring)
            return new_state
    return None

def from_stick2_to_stick3(state):
    new_state = rough_copy(state)
    if new_state[1]:
        if new_state[2] == [] or new_state[2][-1] > new_state[1][-1]:
            ring = new_state[1].pop()
            new_state[2].append(ring)
            return new_state
    return None

def from_stick3_to_stick1(state):
    new_state = rough_copy(state)
    if new_state[2]:
        if new_state[0] == [] or new_state[0][-1] > new_state[2][-1]:
            ring = new_state[2].pop()
            new_state[0].append(ring)
            return new_state
    return None

def from_stick3_to_stick2(state):
    new_state = rough_copy(state)
    if new_state[2]:
        if new_state[1] == [] or new_state[1][-1] > new_state[2][-1]:
            ring = new_state[2].pop()
            new_state[1].append(ring)
            return new_state
    return None

def all_possible_states(state):
    next_states = []
    for move in (from_stick1_to_stick2,from_stick1_to_stick3,from_stick2_to_stick1,from_stick2_to_stick3,from_stick3_to_stick1,from_stick3_to_stick2):
        new_state = move(state)
        if new_state is not None:
            next_states.append(new_state)
    return next_states

def state_to_key(state):
    return tuple(tuple(stick) for stick in state)

def key_to_state(key):
    return [list(stick) for stick in key]

def bfs(start_state):
    queue = [start_state]
    visited = {state_to_key(start_state): None}

    while queue:
        current = queue.pop(0)
        if current == goal_state:
            path = []
            key = state_to_key(current)
            while key is not None:
                path.append(key_to_state(key))
                key = visited[key]
            return path
        for state in all_possible_states(current):
            t = state_to_key(state)
            if t not in visited:
                visited[t] = state_to_key(current)
                queue.append(state)

    return None


def dfs(start_state,depth_limit=None):
    stack = [(start_state, None, 0)]
    visited = set()
    parent = {}

    while stack:
        current, par, depth = stack.pop()
        t = state_to_key(current)
        if t in visited:
            continue
        visited.add(t)
        parent[t] = state_to_key(par) if par is not None else None

        if current == goal_state:
            path = []
            while t is not None:
                path.append(key_to_state(t))
                t = parent[t]
            return path

        if depth_limit is None or depth < depth_limit:
            for next_state in (all_possible_states(current)):
                stack.append((next_state, current, depth + 1))

    return None

if __name__ == "__main__":

    given_state=[[],[],[]]
    used_rings = set()
    valid_state=True
    for i in range(1,4):
        stick_num=int(input(f"place {i} ring on which Stick 1 or 2 or 3: "))
        if stick_num in [1,2,3]:
            ring_num = int(input(f"Enter Ring Size to Be Inserted in Stick{stick_num}: "))
            if ring_num in used_rings:
                print("This ring size already placed!")
                valid_state=False
                break
            used_rings.add(ring_num)
            if stick_num ==1:
                if given_state[0]==[] or given_state[0][-1]>ring_num:
                    given_state[0].append(ring_num)
                else:
                    print("Cannot Insert A Big Ring On Small Ring")
                    valid_state=False
                    break
            elif stick_num==2:
                if given_state[1]==[] or given_state[1][-1]>ring_num:
                    given_state[1].append(ring_num)
                else:
                    print("Cannot Insert A Big Ring On Small Ring" )
                    valid_state=False
                    break
            else:
                if given_state[2]==[] or given_state[2][-1]>ring_num:
                    given_state[2].append(ring_num)
                else:
                    print("Cannot Insert A Big Ring On Small Ring")
                    valid_state=False
                    break
        else:
            print("Choose Correct Stick")
            valid_state=False
            break
    if valid_state:
        print(f"Given State is: {given_state}\n")
        bfs_path=bfs(given_state)
        print("Solution Using Uninformed BFS Search Technique: ")
        for node in reversed(bfs_path):
            print(node)
    
        dfs_path = dfs(given_state)
        print("\nSolution Using Uninformed DFS Search Technique: ")
        for node in reversed(dfs_path):
            print(node)
        print(f"\nSteps Required (BFS): {len(bfs_path)-1}")
        print(f"Steps Required (DFS): {len(dfs_path)-1}")



    
    

    















