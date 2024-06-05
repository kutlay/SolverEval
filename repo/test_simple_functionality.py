import pyomo.environ as pe
from solver_eval.solvers import Solver, AbstractSolver

def test_to_succeed():

    m = pe.ConcreteModel()
    m.x = pe.Var(domain = pe.Binary)
    m.y = pe.Var(domain = pe.Binary)
    m.fx = pe.Var(domain = pe.NonNegativeReals)
    m.fy = pe.Var(domain = pe.NonNegativeReals)
    m.c1 = pe.Constraint(expr = m.fx <= m.x)
    m.c2 = pe.Constraint(expr = m.fy <= m.y)
    m.c3 = pe.Constraint(expr = m.x + m.y <= 1)

    m.obj = pe.Objective(
        expr = m.fx * 0.5 + m.fy * 0.4, 
        sense = pe.maximize,
    )

    opt = AbstractSolver()
    res = opt.solve(m)
    assert res.best_feasible_objective == 0.5

def test_to_fail():

    m = pe.ConcreteModel()
    m.x = pe.Var(domain = pe.Binary)
    m.y = pe.Var(domain = pe.Binary)
    m.fx = pe.Var(domain = pe.NonNegativeReals)
    m.fy = pe.Var(domain = pe.NonNegativeReals)
    m.c1 = pe.Constraint(expr = m.fx <= m.x)
    m.c2 = pe.Constraint(expr = m.fy <= m.y)
    m.c3 = pe.Constraint(expr = m.x + m.y <= 1)

    m.obj = pe.Objective(
        expr = m.fx * 0.5 + m.fy * 0.4, 
        sense = pe.maximize,
    )

    opt = AbstractSolver()
    res = opt.solve(m)
    assert res.best_feasible_objective == 0.4
