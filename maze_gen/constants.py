"""
Binary switches:
- 1 is 0001
- 2 is 0010
- 4 is 0100
- 8 is 1000

Used as ID flags for each direction to
open or close a wall.
"""

NORTH = 1
EAST = 2
SOUTH = 4
WEST = 8

"""
Coordinates for the solver.py to find the
path and display.py to render the path.
"""

MOVEMENTS = {
    NORTH: (0, -1),
    EAST: (1, 0),
    SOUTH: (0, 1),
    WEST: (-1, 0)
}

"""
Opposite directions for the generator.py
to build maze walls.
"""

OPPOSITES = {
    NORTH: SOUTH,
    SOUTH: NORTH,
    EAST: WEST,
    WEST: EAST
}

"""
Simplifies directions into letters for
solver.py to build the final path string.
"""

DIRECTION_LABELS = {
    NORTH: "N",
    EAST: "E",
    SOUTH: "S",
    WEST: "W"
}

"""
ANSI color codes for display.py to render
colors in the terminal.
"""

COLORS = {
    "green": "\033[32m",
    "forest": "\033[38;5;22m",
    "cyan": "\033[36m",
    "magenta": "\033[35m",
    "yellow": "\033[33m",
    "white": "\033[37m",
    "red": "\033[31m",
    "dim": "\033[2m",
    "reset": "\033[0m"
}
