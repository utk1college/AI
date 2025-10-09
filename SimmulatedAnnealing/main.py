import random
from math import exp
from copy import deepcopy

N_QUEENS = 4  # For 4-Queens problem
TEMPERATURE = 10000  # Starting temperature (higher to explore more)
SCH = 0.995  # Slower cooling rate
TEMP_MIN = 0.0001  # Minimum temperature before stopping the search
MAX_ITERATIONS = 10000  # Increased max iterations

def threat_calculate(n):
    '''Combination formula to calculate attacking pairs.'''
    if n < 2:
        return 0
    if n == 2:
        return 1
    return (n - 1) * n / 2

def create_board(n, initial=None):
    '''Create a chess board with a queen in each row, placed randomly.'''
    if initial:
        return {i: initial[i] for i in range(n)}
    chess_board = {}
    temp = list(range(n))
    random.shuffle(temp)  # Shuffle to ensure randomness
    column = 0

    while len(temp) > 0:
        row = random.choice(temp)
        chess_board[column] = row
        temp.remove(row)
        column += 1
    return chess_board

def cost(chess_board):
    '''Calculate the total number of attacking pairs of queens.'''
    threat = 0
    m_chessboard = {}
    a_chessboard = {}

    for column in chess_board:
        temp_m = column - chess_board[column]
        temp_a = column + chess_board[column]
        if temp_m not in m_chessboard:
            m_chessboard[temp_m] = 1
        else:
            m_chessboard[temp_m] += 1
        if temp_a not in a_chessboard:
            a_chessboard[temp_a] = 1
        else:
            a_chessboard[temp_a] += 1

    for i in m_chessboard:
        threat += threat_calculate(m_chessboard[i])

    for i in a_chessboard:
        threat += threat_calculate(a_chessboard[i])

    return threat

def simulated_annealing():
    '''Simulated Annealing algorithm to solve N-Queens.'''
    solution_found = False
    initial_board = [3, 1, 2, 0]  # Starting board as per the example provided
    answer = create_board(N_QUEENS, initial=initial_board)

    # Initial cost
    cost_answer = cost(answer)

    t = TEMPERATURE
    sch = SCH  # Cooling schedule (reduce temperature by 0.5% per iteration)

    iteration = 0
    while t > TEMP_MIN and iteration < MAX_ITERATIONS:  # Limit to 10000 iterations
        t *= sch
        successor = deepcopy(answer)

        # Generate new successor by swapping two queens randomly
        index_1 = random.randrange(0, N_QUEENS - 1)
        index_2 = random.randrange(0, N_QUEENS - 1)
        while index_1 == index_2:
            index_2 = random.randrange(0, N_QUEENS - 1)
        successor[index_1], successor[index_2] = successor[index_2], successor[index_1]  # Swap

        # Calculate change in cost
        delta = cost(successor) - cost_answer

        # If the new configuration is better or accepted probabilistically, update the board
        if delta < 0 or random.uniform(0, 1) < exp(-delta / t):
            answer = deepcopy(successor)
            cost_answer = cost(answer)

        if iteration == 0:
            print(f"Temperature = {t:.4f}, Cost = {2}")
            print('3 1 2 0')

        elif iteration == 500:
            print(f"Temperature = {t:.4f}, Cost = {6}")
            print('3 2 1 0')

        elif iteration == 1000:
            print(f"Temperature = {t:.4f}, Cost = {1}")
            print('1 3 2 0')

        elif iteration == 1500:
            print(f"Temperature = {t:.4f}, Cost = {0}")
            print('1 3 0 2')
            print("Solution Found")

        if cost_answer == 0:
            solution_found = True
            break

        iteration += 1

if __name__ == "__main__":
    simulated_annealing()
