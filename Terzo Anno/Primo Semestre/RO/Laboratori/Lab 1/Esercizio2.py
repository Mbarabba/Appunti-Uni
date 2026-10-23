import pyomo.environ as pyo

#Impostazione del solver 
SOLVER = pyo.SolverFactory('glpk')

#Definizione del modello
model = pyo.ConcreteModel("BIM production planning")

#Definizione delle variabili
model.x = pyo.Var(domain=pyo.NonNegativeReals)
model.y = pyo.Var(domain=pyo.NonNegativeReals)
model.z = pyo.Var(domain=pyo.NonNegativeReals)

#Definisco funzione obiettivo
model.profit = pyo.Objective(expr=model.z, sense=pyo.maximize)

#Definizione vincoli
model.zv1 = pyo.Constraint(expr=model.z <= 12*model.x + 9*model.y)
model.zv2 = pyo.Constraint(expr=model.z <= 11*model.x + 10*model.y)
model.zv3 = pyo.Constraint(expr=model.z <= 8*model.x + 11*model.y)
model.silicon = pyo.Constraint(expr=model.x <= 1000)
model.germanium = pyo.Constraint(expr=model.y <= 1500)
model.plastic = pyo.Constraint(expr=model.x + model.y <= 1750)
model.copper = pyo.Constraint(expr=4 * model.x + 2 * model.y <= 4800)

#Solve
SOLVER.solve(model)

# Stampa i risultati
print(f"x = ({model.x.value:.1f}, {model.y.value:.1f})")
print(f"optimal value = {pyo.value(model.profit):.1f}")
