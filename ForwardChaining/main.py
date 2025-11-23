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
