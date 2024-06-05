import pytest
import os
from enum import Enum

import pyomo.environ as pe
from solver_eval.solvers import Solver, AbstractSolver
from solver_eval.exceptions import SolverNotImplemented, SolverExcluded

def test_abstract_solver_initialization():

    # Simple case
    _ = AbstractSolver(solver=Solver.highs)

    # Simple case from environment variable
    os.environ["SOLVEREVAL_SOLVER"] = "highs"
    _ = AbstractSolver()

    # Selected solver is excluded
    with pytest.raises(SolverExcluded):
        _ = AbstractSolver(solver=Solver.highs, exclude=[Solver.highs])
    
    # Env variable solver is not implemented
    os.environ["SOLVEREVAL_SOLVER"] = "notimplementedsolver"
    with pytest.raises(SolverNotImplemented):
        _ = AbstractSolver()
    

