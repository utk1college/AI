# ---------- Unification Helpers ----------

def is_variable(x):
    """Check if x is a logic variable (lowercase)."""
    return isinstance(x, str) and x.islower()


def occurs_check(var, term, subs):
    """Prevent infinite recursive substitution like x = f(x)."""
    term = substitute(term, subs)
    if var == term:
        return True
    if isinstance(term, tuple):
        return any(occurs_check(var, t, subs) for t in term[1])
    return False


def substitute(term, subs):
    """Apply existing substitutions to a term."""
    if is_variable(term):
        return subs.get(term, term)

    if isinstance(term, tuple):  # function form
        func, args = term
        return (func, [substitute(a, subs) for a in args])

    return term


# ---------- Core Unification Algorithm ----------

def unify(x, y, subs=None):
    """Unify two FOL terms, producing a substitution dictionary or None."""
    if subs is None:
        subs = {}

    x = substitute(x, subs)
    y = substitute(y, subs)

    if x == y:
        return subs

    if is_variable(x):
        if occurs_check(x, y, subs):
            return None
        subs[x] = y
        return subs

    if is_variable(y):
        if occurs_check(y, x, subs):
            return None
        subs[y] = x
        return subs

    if isinstance(x, tuple) and isinstance(y, tuple) and x[0] == y[0] and len(x[1]) == len(y[1]):
        for a, b in zip(x[1], y[1]):
            subs = unify(a, b, subs)
            if subs is None:
                return None
        return subs

    return None


# ---------- Pretty Printing ----------

def pretty_subs(subs):
    if subs is None:
        return "❌ Unification failed"
    if not subs:
        return "✔ Already identical (no substitution needed)"
    return ", ".join(f"{var} → {val}" for var, val in subs.items())


# ---------- Test Cases ----------

tests = [
    ("x", "John"),
    (("Father", ["x"]), ("Father", ["John"])),
    (("Knows", ["John", "x"]), ("Knows", ["y", "Mary"])),
    (("P", ["x", "x"]), ("P", ["John", "Mary"])),  # should fail
    (("Loves", ["x", "y"]), ("Loves", ["Alice", "Bob"])),
    (("F", ["x", "g(y)"]), ("F", ["f(z)", "g(a)"])),
]


# ---------- Run Demonstration ----------

print("\n🧠 First-Order Logic Unification Demo\n")

for i, (a, b) in enumerate(tests, start=1):
    result = unify(a, b)
    print(f"Test {i}:  Unify({a}, {b})")
    print("Result:", pretty_subs(result), "\n")
