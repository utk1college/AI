class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_node(node):
    print(node.value, end=" ")

def dls(root, goal, depth, visited, states_at_depth, path):
    if root is None:
        return None
   
    current_depth = len(path) - 1
    if root not in states_at_depth[current_depth]:
        states_at_depth[current_depth].append(root)
   
    if root.value == goal:
        return path
   
    if depth == 0:
        return None
   
    visited.add(root)
   
    if root.left and root.left not in visited:
        result = dls(root.left, goal, depth - 1, visited, states_at_depth, path + [root.left])
        if result is not None:
            return result
   
    if root.right and root.right not in visited:
        result = dls(root.right, goal, depth - 1, visited, states_at_depth, path + [root.right])
        if result is not None:
            return result
   
    visited.remove(root)
    return None

def iddfs(root, goal, max_depth=3):
    for depth in range(max_depth + 1):  # include max_depth
        visited = set()
        states_at_depth = {d: [] for d in range(depth + 1)}
        print(f"Searching at depth {depth}...")
       
        path = dls(root, goal, depth, visited, states_at_depth, [root])
       
        for d in range(depth + 1):
            for state in states_at_depth[d]:
                print_node(state)
        print()
       
        if path is not None:
            print(f"{goal} Found")
            return
    print("No solution found up to max depth")

# Build tree
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
G = Node("G")
H = Node("H")
I = Node("I")

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
C.right = G
D.left = H
E.left = I

# Run search
iddfs(A, "G", max_depth=3)
