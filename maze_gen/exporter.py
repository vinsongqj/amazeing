"""
MAZE EXPORTER

This file takes the generated maze and saves it
to a .txt file. It converts the grid numbers
into hex characters and records the start and
end coordinates and the solved path string.
The .txt file will be used by another program
to recreate the exact same maze.
"""

from typing import Tuple, Any


class MazeExporter:

    """
    The class used to export maze data to a .txt file.
    """

    def __init__(self, generator: Any) -> None:

        """
        Sets up the exporter with the maze generator.
        """

        self.gen = generator

    def save_to_file(self, filename: str, entry: Tuple[int, int],
                     exit_p: Tuple[int, int]) -> None:

        """
        Saves maze layout and solution to a .txt file.

        1. Creates a new file.
        2. Converts grid numbers into hex and writes.
        3. Writes entry and exit coordinates.
        3. Writes the solution path string.
        """

        try:
            path_str = self.gen.solve(entry, exit_p)

            with open(filename, 'w') as f:
                for y in range(self.gen.height):
                    line = ""
                    for x in range(self.gen.width):
                        val = self.gen.grid[y][x]
                        line += hex(val)[2:].upper()
                    f.write(line + "\n")

                f.write("\n")

                f.write(f"{entry[0]}, {entry[1]}\n")

                f.write(f"{exit_p[0]}, {exit_p[1]}\n")

                f.write(f"{path_str}\n")

            print(f"\nOutput file saved to {filename}")
        except IOError as e:
            print(f"Error saving to {filename}: {e}")
