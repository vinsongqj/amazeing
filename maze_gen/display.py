import os
import sys
import tty
import termios
from typing import Tuple, Any


class MazeRenderer:

    def __init__(self, generator: Any) -> None:
        self.gen = generator
        self.colors = ["\033[32m", "\033[36m", "\033[35m", "\033[33m",
                       "\033[37m"]
        self.c_idx = 0
        self.show_path = False
        self.red = "\033[31m"
        self.dim = "\033[2m"
        self.reset = "\033[0m"

    def _get_char(self) -> str:
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
        return ch

    def _get_path_set(self, start: Tuple[int, int],
                      end: Tuple[int, int]) -> set:
        path_str = self.gen.solve(start, end)
        res = {start}
        cx, cy = start
        move = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}
        for char in path_str:
            dx, dy = move[char]
            cx += dx
            cy += dy
            res.add((cx, cy))
        return res

    def render(self, entry: Tuple[int, int], exit_p: Tuple[int, int]) -> None:

        os.system('clear' if os.name != 'nt' else 'cls')
        c = self.colors[self.c_idx]
        p_set = set()
        if self.show_path:
            p_set = self._get_path_set(entry, exit_p)
        for y in range(self.gen.height):
            top, mid = "", ""
            for x in range(self.gen.width):
                v = self.gen.grid[y][x]
                top += f"{c}████" if (v & 1) else f"{c}█   "
                west = f"{c}█" if (v & 8) else " "
                marker = "   "
                if (x, y) == entry:
                    marker = f"{self.red}███"
                elif (x, y) == exit_p:
                    marker = f"{self.red}███"
                elif (x, y) in self.gen.locked_cells:
                    marker = f"{self.dim}███{self.reset}{c}"
                elif (x, y) in p_set:
                    marker = f"{self.red} • {self.reset}{c}"
                mid += f"{west}{marker}"
            print(f"{top}{c}█{self.reset}")
            print(f"{mid}{c}█{self.reset}")
        print(f"{c}{'████' * self.gen.width}█{self.reset}")

        if self.gen.error_msg:
            print(f"\n\033[91m{self.gen.error_msg}\033[0m")

    def handle_input(self) -> bool:
        print("\n[R] Regen  [P] Path  [C] Color  [Q] Quit")
        ch = self._get_char().lower()
        if ch == "r":
            self.gen.generate()
        elif ch == "p":
            self.show_path = not self.show_path
        elif ch == "c":
            self.c_idx = (self.c_idx + 1) % len(self.colors)
        return ch != "q"
