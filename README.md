*This project has been created as part of the 42 curriculum by ryeong and vgoh.*

# A-Maze-Ing

 ## Description

 A-Maze-Ing is a maze generation algorithm project that generates a solveable maze and includes a reusable package `maze_gen`. 
 
 Our program `a_maze_ing.py` works by reading a user-modified `config.txt` file and generates a maze based on the config parameters using Depth-First Search (Recursive Backtracking) while providing a solution using Breadth-First Search, then displaying it via terminal rendering while listening for user inputs to regenerate the maze / change maze color / display or hide the solution path. It writes a file with the reproducible seed in hexadecimal format upon exit, where each digit encodes which walls are closed, along with the entry and exit coordinates and the path solution string in N/E/S/W format.

 ## Instructions
 ### Requirements
 * Python 3.10+
 * pip
 * venv

 ### Installing the program

 After cloning the repository:

 1. Create the virtual environment and install the dependencies 
    
        make install

 2. Run the program

        make run

3. Additional commands include:
    ```
    make debug        # to debug
    make lint         # to run flake8 and mypy
    make lint-strict  # same as lint but with the --strict flag for mypy
    make clean        # removes build artifacts

4. To run the program without using `make run`:

        python3 a_maze_ing.py config.txt
 



 ### Structure and Format of config.txt

```
# Values can be altered following the key=value format

WIDTH=20               # Number of columns (> 0)
HEIGHT=15              # Number of rows (> 0)
ENTRY=0,0              # Entry coordinates
EXIT=19,14             # Exit coordinates
OUTPUT_FILE=maze.txt   # The file name of the output
PERFECT=True           # Bool that ensures one path if True, and creates loops if False
```

 ## Maze Generation

 ### What Generation Algorithm We Chose And Why

 We went with Depth-First Search based on the table of comparisons below: 
 
| Feature | Depth-First Search  | Kruskal's Algorithm |
| ------------- |:-------------:|:-------------:|
| **Pathing**    | Long, snaking corridors     | Short, branching paths |
| **Dead Ends**     | Few, but long     | Many, but short |
| **Randomness**  | Has a strong directional bias | Unbiased for all directions
| **Difficulty to implement**    | Easy (Uses recursion)     | Hard (Uses disjoint sets) |
**Time Complexity** |  Faster (O(V + E)\) | Slower (O(E log E)) |

Despite the directional bias of DFS and its lack of dead ends, the choice was weighted upon the ease of implementation and time complexity. We also agreed that aesthetically, DFS seemed to fit what we were looking for (long snaking corridors that are easier to follow).

 ## Reusable Sections of Code

 ## Role Delegation

**ryeong**

* Created the config parser.
* Modified the main to handle the parameters parsed and built upon the skeleton.
* Implemented validation and error handling.
* Reviewed code to ensure we were on the right track.
* Edited the readme.

**vgoh**

* Created the maze generator and solver.
* Handled the terminal rendering, output file exporting and user input.
* Built a working skeleton of the main to test maze generation, solving and display.
* Ensuring the .txt output file is written according to subject requirements.
* Editing the readme.

## Planning and Evolution of the Project

## What Worked and What Improved

## Resources

[Graph Traversals - BFS & DFS](https://www.youtube.com/watch?v=pcKY4hjDrxk&list=TLPQMDcwNDIwMjankNRSAo0DTg&index=2)
## Tools Used

**Generative AI** - Used to scrutinize our code for any overlooked error handling and edge cases, and general consultation about the pros and cons of each algorithm how the project should be executed.

**YouTube** - Used to educate ourselves about the topics required to take on the project (Kruskal's and BFS).



