import pyomo.environ as pyo

SOLVER = pyo.SolverFactory('glpk')
model = pyo.ConcreteModel("BIM production planning")

#Definisco le variabili di decisione
model.x1 = pyo.Var(domain=pyo.NonNegativeReals)
model.x2 = pyo.Var(domain=pyo.NonNegativeReals)

#Definisco la funzione obiettivo
model.profit = pyo.Objective(expr=12 * model.x1 + 9 * model.x2, sense=pyo.maximize)

#Definisco i vincoli
model.silicon = pyo.Constraint(expr=model.x1 <= 1000)
model.germanium = pyo.Constraint(expr=model.x2 <= 1500)
model.plastic = pyo.Constraint(expr=model.x1 + model.x2 <= 1750)
model.copper = pyo.Constraint(expr=4 * model.x1 + 2 * model.x2 <= 4800)

# Solve
SOLVER.solve(model)

# Stampa i risultati
print(f"x = ({model.x1.value:.1f}, {model.x2.value:.1f})")
print(f"optimal value = {pyo.value(model.profit):.1f}")