import os
from enum import Enum
from pyomo.contrib.appsi.base import SolverFactory
from pyomo.contrib.appsi.base import (PersistentSolver,PersistentBase)
from .exceptions import SolverExcluded, SolverNotImplemented

class Solver(Enum):
    """
    This enum intends to keep all possible values for a solver. No solver here
    should be removed since it will break during Enum creation and not AbstractSolver
    creation. If you are intending to remove a solver from SolverEval, remove it from
    AbstractSolver instead.
    """
    highs = "highs"
    cbc = "cbc"
    cplex = "cplex"

class AbstractSolver(PersistentBase, PersistentSolver):
    def __new__(self, solver:Solver = None, exclude:list[Solver]=[]):
        
        if solver is not None:
            solver_to_select = solver
        else:
            solver_from_env = os.environ.get('SOLVEREVAL_SOLVER')
            try:
                solver_to_select = Solver(solver_from_env)
            except ValueError:
                raise SolverNotImplemented(f"{solver_from_env} is not implemented in SolverEval")

        if solver_to_select in exclude:
            raise SolverExcluded(f'{solver_to_select} is excluded from the test')

        match solver_to_select:
            case Solver.highs:
                solver = SolverFactory('highs')
            case Solver.cbc:
                solver = SolverFactory('cbc')
            case None:
                raise Exception("No solver selected")
            case _:
                raise SolverNotImplemented(f"{solver_to_select} is not implemented in SolverEval")
        
        return solver