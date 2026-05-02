"""
MAZE SOLVER

This file uses Breadth-First Search (BFS) to find
the shortest path from the start of the maze to
the exit.
"""

from collections import deque
from typing import Tuple, List, Dict
from .constants import MOVEMENTS, DIRECTION_LABELS


class MazeSolver:

    """
    This class calculates the solution for any given maze grid.
    """

    @staticmethod
    def solve(grid: List[List[int]],
              start: Tuple[int, int],
              end: Tuple[int, int]) -> str:

        """
        Finds the shortest path using BFS,
        a search algorithm that spreads out
        in all directions at once, and through
        this method if an exit is found it is the
        absolute shortest path.

        Process:
        1. A queue is created to manage the cells to
           check next, starting from the entry coordinates.
        2. All 4 directions (1, 2, 4, 8) are checked to see
           if there are any open walls.
        3. If a wall is open and unvisited, it is marked as
           visited and the current path is stored.
        4. The search continues spreading out until it hits
           the exit coordinates or runs out of paths.
        """

        if not grid or not grid:
            return ""

        height = len(grid)
        width = len(grid[0])
        curr_x, curr_y = start
        end_x, end_y = end

        if not (0 <= curr_x < width and 0 <= curr_y < height):
            return ""
        if not (0 <= end_x < width and 0 <= end_y < height):
            return ""

        queue = deque([start])
        visited: Dict[Tuple[int, int], str] = {start: ""}

        while queue:
            x, y = queue.popleft()
            if (x, y) == end:
                return visited[(x, y)]

            for bit, (dx, dy) in MOVEMENTS.items():
                if not (grid[y][x] & bit):
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < width and 0 <= ny < height:
                        if (nx, ny) not in visited:
                            direction_char = DIRECTION_LABELS[bit]
                            visited[(nx, ny)] = (visited[(x, y)] +
                                                 direction_char)
                            queue.append((nx, ny))

        return ""
