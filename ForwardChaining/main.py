# --- 🧠 Forward Reasoning in First-Order Logic ---

# Initial facts
facts = {
    "Man(Marcus)",
    "Pompeian(Marcus)"
}

# Rules as (premise, conclusion) pairs
rules = [
    ("Pompeian(x)", "Roman(x)"),
    ("Roman(x)", "Loyal(x)"),
    ("Man(x)", "Person(x)"),
    ("Person(x)", "Mortal(x)")
]


def forward_chain(facts, rules):
    """
    Simple forward chaining for ground (variable-free) first-order logic.
    """
    inferred = set(facts)  # Known facts
    changed = True
    step = 1

    print("🔍 Starting Forward Reasoning...\n")
    print("Initial facts:")
    for f in inferred:
        print(f"  • {f}")
    print("\n--- Reasoning Steps ---")

    while changed:
        changed = False
        for premise, conclusion in rules:
            # Match premise predicate, e.g., Pompeian(x)
            pred_name = premise.split("(")[0]

            # Search for matching facts, e.g., Pompeian(Marcus)
            for fact in list(inferred):
                if fact.startswith(pred_name + "("):
                    constant = fact[fact.find("(")+1 : fact.find(")")]
                    new_fact = conclusion.replace("x", constant)

                    if new_fact not in inferred:
                        inferred.add(new_fact)
                        changed = True
                        print(f" Step {step}: {premise.replace('x', constant)}  ⟹  {new_fact}")
                        step += 1

    print("\n✅ Forward chaining complete.\n")
    return inferred


# Run the inference
derived_facts = forward_chain(facts, rules)

# Query to prove
query = "Mortal(Marcus)"
print("🧩 Query:", query)

# Check result
if query in derived_facts:
    print(f"✅ Result: {query} was successfully derived!")
else:
    print(f"❌ Result: {query} could NOT be derived.")

image.png


On Thu, Nov 6, 2025 at 1:13 PM Utkrisht Umang <utkrisht.cs23@bmsce.ac.in> wrote:
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
