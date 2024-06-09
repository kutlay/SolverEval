# SolverEval

SolverEval is a project to continuously test mathematical solvers. It faciliates an open environment for model developers to add real world optimization problems to a repository and tests them peridocally against different versions of mathematical solvers.

SolverEval benefits the optimization community by:

- Creating a common repository to track performance of mathematical solvers against real world optimization problems
- Periodically testing the problem repository using new versions of mathematical solvers and catching regression bugs
- Providing reports to solver developers to save time in testing and catch problems sooner

# Solvers included on SolverEval

Standardization is key to keep a growing repository of tests manageable. SolverEval uses [pyomo](https://github.com/Pyomo/pyomo) to standardize the models to test. This means that any **open source** solver that has a maintained interface on pyomo can be included in SolverEval.

Since SolverEval's purpose is to test the solvers and not the interface communicating with the solvers, we keep the latest stable version of `pyomo` as the modeling interface.

The current list of available solvers on SolverEval:

- HiGHS (Currently broken due to SolverFactory in pyomo)
- CBC