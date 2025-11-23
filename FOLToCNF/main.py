from sympy import symbols, Or
from sympy.logic.boolalg import to_cnf

# Step 1: Define Boolean symbols
A = symbols('Animal_f1x', boolean=True)
B = symbols('Loves_x_f1x', boolean=True)
C = symbols('Loves_f2x_x', boolean=True)

# Step 2: Build logical expression (A ∨ B ∨ C)
expr = Or(A, B, C)

# Step 3: Convert to CNF
cnf_expr = to_cnf(expr, simplify=True)

# Step 4: Custom pretty print mapping
pretty_map = {
    A: "Animal(f₁(x))",
    B: "Loves(x, f₁(x))",
    C: "Loves(f₂(x), x)"
}

def pretty(expr):
    text = str(expr)
    for sym, rep in pretty_map.items():
        text = text.replace(str(sym), rep)
    text = (
        text.replace('|', ' ∨ ')
            .replace('&', ' ∧ ')
            .replace('~', '¬')
    )
    return f"⟦ {text} ⟧"

# Step 5: Print nice-looking CNF
print("\n🧩 CNF Formula:")
print(pretty(cnf_expr))
