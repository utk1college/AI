import itertools
import pandas as pd

# Define propositional variables
vars = ['Q', 'P', 'R']

# Helper function for implication
def implies(a, b):
    return (not a) or b

# Define formulas in KB
def formula_Q_implies_P(Q, P, R):
    return implies(Q, P)

def formula_P_implies_notQ(Q, P, R):
    return implies(P, not Q)

def formula_Q_or_R(Q, P, R):
    return Q or R

# Define KB and entailment formulas
def KB(Q, P, R):
    return formula_Q_implies_P(Q, P, R) and formula_P_implies_notQ(Q, P, R) and formula_Q_or_R(Q, P, R)

def entail_R(Q, P, R):
    return R

def entail_R_implies_P(Q, P, R):
    return implies(R, P)

def entail_Q_implies_R(Q, P, R):
    return implies(Q, R)

# Generate truth table (TTT → FFF order)
rows = []
# reversed order: True > False
for Q, P, R in itertools.product([True, False], repeat=3):
    q_imp_p = formula_Q_implies_P(Q, P, R)
    p_imp_notq = formula_P_implies_notQ(Q, P, R)
    q_or_r = formula_Q_or_R(Q, P, R)
    kb_val = KB(Q, P, R)

    rows.append({
        'Q': Q, 'P': P, 'R': R,
        'Q→P': q_imp_p,
        'P→¬Q': p_imp_notq,
        'Q∨R': q_or_r,
        'KB True?': kb_val,
        'R→P': entail_R_implies_P(Q, P, R),
        'Q→R': entail_Q_implies_R(Q, P, R)
    })

# Convert to DataFrame
df = pd.DataFrame(rows)

# Sort in descending order of Q, then P, then R (TTT first → FFF last)
df = df.sort_values(by=['Q', 'P', 'R'], ascending=[False, False, False]).reset_index(drop=True)

# Display the truth table
print("Truth Table for KB:")
print(df.to_string(index=False))

# Models where KB is true
models = df[df['KB True?'] == True]
print("\nModels where KB is True:")
print(models[['Q', 'P', 'R']].to_string(index=False))

# Entailment function
def entails(kb_models, formula):
    return all(formula(Q, P, R) for Q, P, R in kb_models[['Q', 'P', 'R']].itertuples(index=False))

# Evaluate entailments
entail_R_val = entails(models, lambda Q, P, R: entail_R(Q, P, R))
entail_R_imp_P_val = entails(models, lambda Q, P, R: entail_R_implies_P(Q, P, R))
entail_Q_imp_R_val = entails(models, lambda Q, P, R: entail_Q_implies_R(Q, P, R))

print("\nEntailment Results:")
print(f"KB ⊨ R       ? {entail_R_val}")
print(f"KB ⊨ (R→P)   ? {entail_R_imp_P_val}")
print(f"KB ⊨ (Q→R)   ? {entail_Q_imp_R_val}")
