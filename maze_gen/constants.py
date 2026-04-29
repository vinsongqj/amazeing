NORTH = 1
EAST = 2
SOUTH = 4
WEST = 8

MOVEMENTS = {
    NORTH: (0, -1),
    EAST: (1, 0),
    SOUTH: (0, 1),
    WEST: (-1, 0)
}

OPPOSITES = {
    NORTH: SOUTH,
    SOUTH: NORTH,
    EAST: WEST,
    WEST: EAST
}

DIRECTION_LABELS = {
    NORTH: "N",
    EAST: "E",
    SOUTH: "S",
    WEST: "W"
}

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
