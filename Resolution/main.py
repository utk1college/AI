from itertools import combinations

# ---------- Pretty Printer ----------
def pretty_literal(lit):
    pred, args = lit
    neg = pred.startswith("~")
    pred = pred[1:] if neg else pred
    return f"¬{pred}({', '.join(args)})" if neg else f"{pred}({', '.join(args)})"

def pretty_clause(clause):
    return " ∨ ".join(pretty_literal(l) for l in clause) if clause else "□"

# ---------- Unification ----------
def unify(a, b, subs=None):
    subs = subs or {}
    if a == b: return subs
    if isinstance(a, str) and a.islower(): return unify_var(a, b, subs)
    if isinstance(b, str) and b.islower(): return unify_var(b, a, subs)
    if isinstance(a, tuple) and isinstance(b, tuple) and a[0] == b[0]:
        for x, y in zip(a[1], b[1]):
            subs = unify(x, y, subs)
            if subs is None: return None
        return subs
    return None

def unify_var(var, val, subs):
    if var in subs: return unify(subs[var], val, subs)
    if val in subs: return unify(var, subs[val], subs)
    subs[var] = val
    return subs

# ---------- Resolution ----------
def apply_subs(clause, subs):
    return [(pred, tuple(subs.get(arg, arg) for arg in args)) for pred, args in clause]

def resolve(c1, c2):
    for lit1 in c1:
        for lit2 in c2:
            if lit1[0] == "~" + lit2[0] or lit2[0] == "~" + lit1[0]:
                subs = unify(lit1[1], lit2[1])
                if subs is not None:
                    new_clause = (set(apply_subs(c1, subs)) | set(apply_subs(c2, subs))) - {lit1, lit2}
                    return frozenset(new_clause)
    return None

# ---------- Resolution Engine ----------
def resolution(kb, query, verbose=False):
    kb = set(kb)
    kb.add(frozenset({('~Likes', query[1])}))  # Negated goal

    print("🔍 Proving query:", pretty_literal(("Likes", query[1])))
    print("\n--- Resolution Process ---")

    step = 1

    while True:
        new_clauses = set()

        for c1, c2 in combinations(kb, 2):
            resolvent = resolve(c1, c2)

            if resolvent is not None:
                if verbose or step <= 8:  # limit printing if verbose=False
                    print(f" Step {step}: {pretty_clause(c1)}  ⟹  {pretty_clause(c2)}  →  {pretty_clause(resolvent)}")

                if not resolvent:
                    print("\n✅ Conclusion: Empty clause reached → QUERY PROVEN TRUE!")
                    return True

                new_clauses.add(resolvent)
                step += 1

        if new_clauses.issubset(kb):
            print("\n❌ No new resolvents → Query cannot be proven.")
            return False

        kb |= new_clauses


# ---------- Knowledge Base ----------
KB = [
    frozenset({('~Food', ('x',)), ('Likes', ('John', 'x'))}),
    frozenset({('Food', ('Apple',))}),
    frozenset({('Food', ('Vegetable',))}),
    frozenset({('~Eats', ('x','y')), ('Killed', ('x',)), ('Food', ('y',))}),
    frozenset({('Eats', ('Anil', 'Peanut'))}),
    frozenset({('Alive', ('Anil',))}),
    frozenset({('~Eats', ('Anil','y')), ('Eats', ('Harry','y'))}),
    frozenset({('~Alive', ('x',)), ('~Killed', ('x',))}),
    frozenset({('Killed', ('x',)), ('Alive', ('x',))})
]

# ---------- Run ----------
resolution(KB, ('Likes', ('John', 'Peanut')), verbose=False)
