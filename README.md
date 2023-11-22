# Sudoku Solver

This Python project provides a Sudoku solver using a backtracking algorithm. Given a Sudoku puzzle, the code attempts to find a solution and modifies the grid in place.

## Usage

1. Make sure you have Python installed on your system. You can download Python from [here](https://www.python.org/downloads/).

2. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/sudoku-solver.git

   Navigate to the project directory:

   cd sudoku-solver

   Run the Sudoku solver script:

   python project.py

   or for Python 3:

   python3 project.py

3. If a solution exists, the solved Sudoku grid will be displayed in the terminal. If no solution exists, a corresponding message will be printed.

Example 1:

grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 8, 0, 0, 7, 9, 5]
]

Will console out "No solution exists."

whereas Example 2:

grid = [
    [0, 3, 4, 6, 0, 8, 9, 1, 0],
    [0, 7, 2, 1, 9, 5, 3, 4, 8],
    [0, 9, 8, 3, 4, 2, 5, 6, 7],
    [0, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 0, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 0, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 0, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 0, 9, 6, 3, 5],
    [3, 4, 50, 2, 8, 0, 1, 7, 9]
]

will console out solution

5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 50 2 8 6 1 7 9
