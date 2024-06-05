class SolverEvalException(Exception):
    pass

class SolverExcluded(SolverEvalException):
    pass

class SolverNotImplemented(SolverEvalException):
    pass