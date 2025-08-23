MAX = 1  # Maximizing player (AI, X)
MIN = -1 # Minimizing player (You, O)
infinity = float('inf')

def game_over(state):
    """Checks if the game is over (either win or draw)."""
    return winner(state) is not None or len(empty_cells(state)) == 0

def winner(state):
    """Returns the winner (MAX or MIN), or None if there's no winner."""
    lines = []
    lines.extend(state)  # rows
    lines.extend([[state[r][c] for r in range(3)] for c in range(3)])  # columns
    lines.append([state[i][i] for i in range(3)])  # diagonal
    lines.append([state[i][2 - i] for i in range(3)])  # anti-diagonal

    for line in lines:
        if line == [MAX, MAX, MAX]:
            return MAX
        elif line == [MIN, MIN, MIN]:
            return MIN
    return None

def evaluate(state):
    """Evaluates the board and returns +10 for MAX win, -10 for MIN win, or 0."""
    w = winner(state)
    if w == MAX:
        return 10
    elif w == MIN:
        return -10
    else:
        return 0

def empty_cells(state):
    """Returns a list of empty cells on the board."""
    cells = []
    for x in range(3):
        for y in range(3):
            if state[x][y] == 0:
                cells.append((x, y))
    return cells

def minimax(state, depth, player, cost=0):
    """Minimax algorithm to find the best move, returns the move with its score and cost."""
    if player == MAX:
        best = [-1, -1, -infinity, cost]
    else:
        best = [-1, -1, +infinity, cost]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score, cost]

    for cell in empty_cells(state):
        x, y = cell
        state[x][y] = player
        score = minimax(state, depth - 1, -player, cost + 1)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == MAX:
            if score[2] > best[2]:
                best = score
        else:
            if score[2] < best[2]:
                best = score

    return best

def print_board(state):
    """Prints the game board."""
    symbols = {MAX: 'X', MIN: 'O', 0: '-'}
    for row in state:
        print(" ".join(symbols[cell] for cell in row))
    print()

def player_move(state):
    """Prompts the player for a move and validates the input."""
    while True:
        try:
            move = input("Enter your move (row and column: 0 1): ").split()
            if len(move) != 2:
                print("Please enter two numbers separated by space.")
                continue
            x, y = int(move[0]), int(move[1])
            if x not in range(3) or y not in range(3):
                print("Coordinates must be between 0 and 2.")
                continue
            if state[x][y] != 0:
                print("Cell already occupied. Choose another.")
                continue
            return x, y
        except ValueError:
            print("Invalid input. Enter numbers like: 0 2")

# Initial empty board
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

print("You are O, AI is X")
print_board(board)

total_cost = 0  # Track total cost in terms of moves

while True:
    # Player move
    x, y = player_move(board)
    board[x][y] = MIN
    total_cost += 1
    print("Your move:")
    print_board(board)

    if game_over(board):
        break

    # AI move
    print("AI is thinking...")
    x, y, score, cost = minimax(board, depth=9, player=MAX, cost=total_cost)
    board[x][y] = MAX
    total_cost = cost
    print(f"AI moves at {x}, {y}")
    print_board(board)

    if game_over(board):
        break

# Determine the winner
w = winner(board)
if w == MAX:
    print(f"AI (X) wins! Total cost: {total_cost}")
elif w == MIN:
    print(f"You (O) win! Total cost: {total_cost}")
else:
    print(f"It's a draw! Total cost: {total_cost}")

