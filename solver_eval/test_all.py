from dataclasses import dataclass
import glob
import importlib
from inspect import isfunction
from pathlib import Path

import os
from pathlib import Path
import numpy as np
import importlib.util
import inspect
from timeit import default_timer as timer

import solver_eval.exceptions

@dataclass
class ExecutionStatistics():
    samples: int
    average: float
    p50: float
    p95: float
    p99: float

def load_tests_from_module(module):
    """Load test functions from a given module."""
    for name, func in inspect.getmembers(module, inspect.isfunction):
        if name.startswith("test_"):
            yield func


def load_modules_from_folder(folder):
    """Load modules from a given folder."""
    for filename in os.listdir(folder):
        if filename.startswith("test_") and filename.endswith(".py"):
            filepath = os.path.join(folder, filename)
            spec = importlib.util.spec_from_file_location(
                filename[:-3], filepath)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            yield module


def time_function(func, sample: int = 10) -> list[float]:
    """
    Time the given function for `sample` times and return in a list
    """

    execution_times = []

    for i in range(sample):
        start = timer()
        result = func()
        end = timer()
        execution_times.append(end-start)

    return execution_times


def get_stats(execution_times: list[float]) -> ExecutionStatistics:
    """
    Get stats from a list of execution times
    """

    execution_times = np.array(execution_times)

    stats = ExecutionStatistics(
        samples = len(execution_times),
        average = np.average(execution_times),
        p50 = np.percentile(execution_times, 50),
        p95 = np.percentile(execution_times, 95),
        p99 = np.percentile(execution_times, 99)
    )

    return stats


def run_tests():
    """Discover and run all test functions."""
    test_folder = os.path.join(Path(__file__).parent.parent, "repo")
    modules = load_modules_from_folder(test_folder)
    all_tests = []

    for module in modules:
        tests = list(load_tests_from_module(module))
        all_tests.extend(tests)

    passed = 0
    failed = 0
    excluded = 0

    for test in all_tests:
        try:
            execution_times = time_function(test)
            stats = get_stats(execution_times)
            print(stats)
            print(f"{test.__name__} ... PASSED")
            passed += 1
        except solver_eval.exceptions.SolverEvalException as exception:
            print(f"{test.__name__} ... EXCLUDED: {exception}")
            excluded += 1
        except Exception as exception:
            print(f"{test.__name__} ... FAILED: {exception}")
            failed += 1

    print(f"\nTotal tests: {len(all_tests)}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Excluded: {excluded}")


if __name__ == "__main__":
    run_tests()
