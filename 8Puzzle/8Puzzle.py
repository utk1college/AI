from collections import deque

# Goal state as tuple
goal_state = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)   # 0 = blank

# Moves: up, down, left, right
moves = [(-1,0), (1,0), (0,-1), (0,1)]

def get_blank_pos(state):
    idx = state.index(0)
    return divmod(idx, 3)  # (row, col)

def is_goal(state):
    return state == goal_state

def possible_moves(state):
    x, y = get_blank_pos(state)
    idx = x * 3 + y
    neighbors = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            nidx = nx * 3 + ny
            new_state = list(state)
            new_state[idx], new_state[nidx] = new_state[nidx], new_state[idx]
            neighbors.append(tuple(new_state))
    return neighbors

def brute_force(initial_state):
    queue = deque([(initial_state, 0)])  # (state, steps)
    visited = set()

    while queue:
        state, steps = queue.popleft()  # BFS
        if state in visited:
            continue
        visited.add(state)

        if is_goal(state):
            return steps

        for neighbor in possible_moves(state):
            if neighbor not in visited:
                queue.append((neighbor, steps + 1))

    return -1  # no solution

def print_state(state):
    """Pretty print 3x3 puzzle state"""
    for i in range(0, 9, 3):
        row = [" " if x == 0 else str(x) for x in state[i:i+3]]
        print(" ".join(row))
    print()

# ---- MAIN ----
if __name__ == "__main__":
    # Predefined test cases
    test_cases = {
        "Best case (already solved)": (1, 2, 3,
                                       4, 5, 6,
                                       7, 8, 0),

        "Average case (medium shuffle)": (1, 2, 3,
                                          4, 5, 6,
                                          0, 7, 8),

        "Worst case (heavily scrambled)": (8, 6, 7,
                                           2, 5, 4,
                                           3, 0, 1)
    }

    for name, state in test_cases.items():
        print(f"{name} - Initial State:")
        print_state(state)
        steps = brute_force(state)
        if steps != -1:
            print(f"→ Solved in {steps} steps!\n")
        else:
            print("→ No solution found.\n")
