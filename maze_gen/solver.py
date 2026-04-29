from collections import deque
from typing import Tuple, List, Dict
from .constants import MOVEMENTS, DIRECTION_LABELS


class MazeSolver:

    @staticmethod
    def _get_d_char(d: int) -> str:
        mapping = {1: "N", 2: "E", 4: "S", 8: "W"}
        return mapping.get(d, "")

    @staticmethod
    def solve(grid: List[List[int]],
              start: Tuple[int, int],
              end: Tuple[int, int]) -> str:

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
