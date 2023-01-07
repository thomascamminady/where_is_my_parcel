from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, TypeVar


class Solution(ABC):
    pass


class AnalyticalSolution(Solution):
    pass


class NumericalSolution(Solution):
    def get_mesh_size(self) -> float:
        return 0.12345


SolutionGeneric = TypeVar("SolutionGeneric", bound=Solution)


class Solver(ABC, Generic[SolutionGeneric]):
    @abstractmethod
    def _solve(self, task: int) -> SolutionGeneric:
        pass

    def solve(self, task: int) -> SolutionGeneric:
        return self._solve(task)


class NumericalSolver(Solver[NumericalSolution]):
    def _solve(self, task: int) -> NumericalSolution:
        return NumericalSolution()


class AnalyticalSolver(Solver[AnalyticalSolution]):
    def _solve(self, task: int) -> AnalyticalSolution:
        return AnalyticalSolution()


if __name__ == "__main__":
    solver = NumericalSolver()
    solution = solver.solve(1)
    print(solution.get_mesh_size())
