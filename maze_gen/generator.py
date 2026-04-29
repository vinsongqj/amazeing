import random
from typing import List, Tuple, Set, Optional
from .constants import MOVEMENTS, NORTH, EAST, SOUTH, WEST, OPPOSITES
from .solver import MazeSolver


class MazeGenerator:

    def __init__(self, width: int, height: int,
                 seed: Optional[int] = None) -> None:
        self.width = width
        self.height = height
        self.error_msg = ""
        self.grid: List[List[int]] = []
        self.locked_cells: Set[Tuple[int, int]] = set()
        if seed is not None:
            random.seed(seed)

    def _apply_42_mask(self) -> None:

        self.locked_cells.clear()
        mx = self.width // 2
        my = self.height // 2
        offsets = [
            (-4, -2), (-4, -1), (-4, 0), (-3, 0), (-2, 0), (-2, 1), (-2, 2),

            (0, -2), (1, -2), (2, -2), (2, -1), (2, 0), (1, 0),
            (0, 0), (0, 1), (0, 2), (1, 2), (2, 2)
        ]
        for dx, dy in offsets:
            tx = mx + dx
            ty = my + dy
            if 0 <= tx < self.width and 0 <= ty < self.height:
                self.locked_cells.add((tx, ty))

    def generate(self, perfect: bool = True, use_logo: bool = True) -> None:

        self.locked_cells.clear()
        self.error_msg = ""

        if use_logo:
            if self.width < 15 or self.height < 10:
                self.error_msg = ("Error: Maze must be at least 15x10 "
                                  "to generate 42 pattern.")
            else:
                self._apply_42_mask()

        full_block = NORTH | EAST | SOUTH | WEST
        self.grid = [[full_block for _ in range(self.width)]
                     for _ in range(self.height)]

        parent = list(range(self.width * self.height))

        def find(i: int) -> int:
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        walls = []
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in self.locked_cells:
                    continue

                for direction in [EAST, SOUTH]:
                    dx, dy = MOVEMENTS[direction]
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        if (nx, ny) not in self.locked_cells:
                            walls.append((x, y, nx, ny, direction))

        random.shuffle(walls)

        for x1, y1, x2, y2, d in walls:
            r1 = find(y1 * self.width + x1)
            r2 = find(y2 * self.width + x2)

            if r1 != r2:
                parent[r1] = r2
                self.grid[y1][x1] &= ~d
                self.grid[y2][x2] &= ~OPPOSITES[d]
            elif not perfect and random.random() < 0.1:
                self.grid[y1][x1] &= ~d
                self.grid[y2][x2] &= ~OPPOSITES[d]

    def solve(self, start: Tuple[int, int] = (0, 0),
              end: Optional[Tuple[int, int]] = None):
        if end is None:
            end = (self.width - 1, self.height - 1)
        return MazeSolver.solve(self.grid, start, end)
