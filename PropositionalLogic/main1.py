import itertools

# Define the propositional formulas as functions
def alpha(A, B):
    return A or B  # A ∨ B

def KB(A, B, C):
    return (A or C) and (B or not C)  # (A ∨ C) ∧ (B ∨ ¬C)

# Generate all possible truth assignments for A, B, and C
truth_values = [False, True]
assignments = list(itertools.product(truth_values, repeat=3))

# Iterate through each assignment and evaluate alpha and KB
print("A B C  A∨C  B∨¬C  KB  α  KB => α")
for assignment in assignments:
    A, B, C = assignment
    a_or_c = A or C
    b_or_not_c = B or not C
    kb = KB(A, B, C)
    alpha_val = alpha(A, B)
    
    # Print the values in a row format, with true/false corresponding to each formula
    implies = kb == alpha_val  # KB => α (whether KB implies α)
    print(f"{A} {B} {C}  {a_or_c} {b_or_not_c}  {kb}  {alpha_val} {'true' if implies else 'false'}")
