import heapq

# Goal state
GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Directions for moving the blank space (left, right, up, down)
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Manhattan Distance Heuristic
def manhattan_distance(state):
    distance = 0
    for i, val in enumerate(state):
        if val == 0:
            continue
        goal_pos = GOAL.index(val)
        curr_row, curr_col = divmod(i, 3)
        goal_row, goal_col = divmod(goal_pos, 3)
        distance += abs(curr_row - goal_row) + abs(curr_col - goal_col)
    return distance

# Get neighbors by moving the blank space
def get_neighbors(state):
    blank_idx = state.index(0)
    blank_row, blank_col = divmod(blank_idx, 3)
    neighbors = []
    
    for move in MOVES:
        new_row, new_col = blank_row + move[0], blank_col + move[1]
        
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank_idx = new_row * 3 + new_col
            new_state = list(state)
            new_state[blank_idx], new_state[new_blank_idx] = new_state[new_blank_idx], new_state[blank_idx]
            neighbors.append(tuple(new_state))
    
    return neighbors

# A* Algorithm
def a_star(start):
    open_list = []
    heapq.heappush(open_list, (manhattan_distance(start), start))  # (f, state)
    g_score = {start: 0}
    f_score = {start: manhattan_distance(start)}
    came_from = {}

    while open_list:
        _, current = heapq.heappop(open_list)
        
        if current == GOAL:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        for neighbor in get_neighbors(current):
            tentative_g_score = g_score[current] + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                h_score = manhattan_distance(neighbor)
                f_score[neighbor] = tentative_g_score + h_score
                heapq.heappush(open_list, (f_score[neighbor], neighbor))

                # Print current state, g, h, and f values
                print(f"Current State: {neighbor}")
                print_board(neighbor)
                print(f"g: {tentative_g_score}, h: {h_score}, f: {f_score[neighbor]}")
    
    return None  # No solution found

# Function to print the board
def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

# Example Run
start_state = (1, 2, 3, 4, 0, 5, 7, 8, 6)  # Initial state
solution = a_star(start_state)

if solution:
    print("Solution found!")
    for step in solution:
        print(step)
        print_board(step)
else:
    print("No solution.")
