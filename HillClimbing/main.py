def hill_climbing_specific_example():
    board = [3, 1, 2, 0]  # Starting board
    
    print("Initial board:", board)
    print("Initial cost:", calculate_cost(board))
    
    iteration = 1
    while iteration <= 2:
        print(f"\nIteration {iteration}:")
        
        neighbors = generate_neighbors(board)
        neighbor_costs = [(neighbor, calculate_cost(neighbor)) for neighbor in neighbors]
        
        for idx, (neighbor, cost) in enumerate(neighbor_costs):
            print(f"Neighbor {idx + 1}: {neighbor}, Cost: {cost}")
        
        best_neighbor, best_cost = min(neighbor_costs, key=lambda x: x[1])
        
        if best_cost >= calculate_cost(board):
            print("\nNo improvement found, stopping.")
            break
        
        board = best_neighbor
        print(f"New board: {board}, Cost: {best_cost}")
        
        iteration += 1
    
    print("\nFinal solution:")
    print(f"Board: {board}")
    print(f"Cost: {calculate_cost(board)}")

# Helper functions reused from before
import random

def calculate_cost(board):
    n = len(board)
    cost = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                cost += 1
    return cost

def generate_neighbors(board):
    neighbors = []
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            neighbor = board[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

# Run the example
hill_climbing_specific_example()
