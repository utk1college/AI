from collections import deque

GOAL = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 0))

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def print_state(state):
    for row in state:
        print(' '.join(str(x) for x in row))
    print()

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def swap_positions(state, pos1, pos2):
    state_list = [list(row) for row in state]
    r1, c1 = pos1
    r2, c2 = pos2
    state_list[r1][c1], state_list[r2][c2] = state_list[r2][c2], state_list[r1][c1]
    return tuple(tuple(row) for row in state_list)

def get_neighbors(state):
    neighbors = []
    zero_pos = find_zero(state)
    for move in MOVES:
        new_r = zero_pos[0] + move[0]
        new_c = zero_pos[1] + move[1]
        if 0 <= new_r < 3 and 0 <= new_c < 3:
            new_state = swap_positions(state, zero_pos, (new_r, new_c))
            neighbors.append(new_state)
    return neighbors

def dls(state, goal, depth, visited, states_at_depth, path):
    # path is list of states from start to current
    current_depth = len(path) - 1
    states_at_depth[current_depth].append(state)
   
    if state == goal:
        return path  # solution path
   
    if depth == 0:
        return None
   
    visited.add(state)
   
    for neighbor in get_neighbors(state):
        if neighbor not in visited:
            result = dls(neighbor, goal, depth - 1, visited, states_at_depth, path + [neighbor])
            if result is not None:
                return result
    visited.remove(state)
    return None

def iddfs(start, goal, max_depth=50):
    for depth in range(max_depth):
        visited = set()
        states_at_depth = {d: [] for d in range(depth+1)}
        print(f"Searching at depth {depth}...")
        path = dls(start, goal, depth, visited, states_at_depth, [start])
       
        # Print states visited at each depth
        for d in range(depth+1):
            print(f"Depth {d}:")
            for state in states_at_depth[d]:
                print_state(state)
       
        if path is not None:
            print(f"Solution found at depth {depth}")
            print("Solution path:")
            for d, state in enumerate(path):
                print(f"Depth {d}:")
                print_state(state)
            return
    print("No solution found up to max depth")

# Start state tuple
start_state = ((1, 2, 3),
               (4, 5, 6),
               (0, 7, 8))

iddfs(start_state, GOAL)
