from typing import Tuple, Any


class MazeExporter:

    def __init__(self, generator: Any) -> None:
        self.gen = generator

    def save_to_file(self, filename: str, entry: Tuple[int, int],
                     exit_p: Tuple[int, int]) -> None:

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
