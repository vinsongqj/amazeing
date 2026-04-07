import random
from typing import List, Tuple


class MazeGenerator:

    def __init__(self, width: int, height: int, seed: int = None):

        self.width = width
        self.height = height
        self.seed = seed
        self.grid = [[15 for _ in range(width)] for _ in range(height)]

        if seed is not None:
            random.seed(seed)


    def _depth_first_search(self, start_x: int, start_y: int) -> None
        
        stack = [(start_x, start_y)]
        self.visited[start_y][start_x] = True

        while stack:
            x, y = stack[-1]
            
            neighbors = [
                ("N", 0, -1, 1, 4), ("E", 1, 0, 2, 8 ),
                ("S", 0, 1, 4, 1), ("W", -1, 0, 8, 2)
            ]

            random.shuffle(neighbors)

            found_neighbor = False
            for _, dx, dy, wall_bit, opp_bit in neighbors:
                nx, ny = x + dx, y + dy

                if 0 <= nx < self.width and 0 <= ny < self.height and not self.visited[ny][nx]:
                    self.grid[y][x] &= ~wall_bit
                    self.grid[ny][nx] &= ~opp_bit
                    self.visited[ny][nx] = True
                    stack.append((nx, ny))
                    found_neighbor = True
                    break

                if not found_neighbor:
                    stack.pop()

    
    def _kruskal(self) -> None

        parent = {(x, y): (x, y) for x in range(self.width) for y in range(self.height)}
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j):
            root_i, root_j = find(i), find(j)

            if root_i != root_j:
                parent[root_i] = root_j
                return True

            return False
        
        walls = self._get_all_internal_walls()
        random.shuffle(walls)

        for wall in walls:
            cell1, cell2, wall_bit, opp_bit = wall
            if union(cell1, cell2):
                self.grid[cell1[1]][cell1[0]] &= ~wall_bit
                self.grid[cell2[1]][cell2[0]] &= ~opp_bit
        

    def generate(self, algorithm: str = "DFS"):
        self._42_pattern()

        if algorithm.upper() == "DFS":
            self._run_dfs(0, 0)
        elif algorithm.upper() == "KRUSKAL":
            self._run_kruskal()
        
        self._border()