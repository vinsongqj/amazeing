import sys
from maze_gen.generator import MazeGenerator
from maze_gen.display import MazeRenderer
from maze_gen.exporter import MazeExporter


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py config.txt")
        return

    cfg = {
        "WIDTH": 20,
        "HEIGHT": 15,
        "ENTRY": (0, 0),
        "EXIT": (19, 14),
        "PERFECT": True,
        "OUTPUT": "maze.txt"
    }

    gen = MazeGenerator(cfg["WIDTH"], cfg["HEIGHT"])

    gen.generate(perfect=cfg["PERFECT"], use_logo=True)

    ui = MazeRenderer(gen)
    exporter = MazeExporter(gen)

    try:
        while True:
            ui.render(cfg["ENTRY"], cfg["EXIT"])

            if not ui.handle_input():
                exporter.save_to_file(
                    cfg["OUTPUT"],
                    cfg["ENTRY"],
                    cfg["EXIT"]
                )
                break
    except KeyboardInterrupt:
        print("\nSimulation interrupted.")
    finally:
        print("Exiting A-Maze-ing")


if __name__ == "__main__":
    main()
