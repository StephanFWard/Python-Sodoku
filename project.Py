def is_valid_move(grid, row, col, num):
    # Check if 'num' is not in the current row, column, and 3x3 subgrid
    return (
        all(num != grid[row][i] for i in range(9)) and
        all(num != grid[i][col] for i in range(9)) and
        all(num != grid[row // 3 * 3 + i // 3][col // 3 * 3 + i % 3] for i in range(9)
        )
    )

def solve_sudoku(grid):
    empty_cell = find_empty_cell(grid)
    
    if not empty_cell:
        # No empty cells left, puzzle is solved
        return True
    
    row, col = empty_cell
    
    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            # If placing 'num' in the current position doesn't lead to a solution,
            # backtrack and try the next number
            grid[row][col] = 0
    
    # No valid number was found, backtrack to the previous state
    return False

def find_empty_cell(grid):
    # Find the first empty cell (cell with value 0)
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

# Example Usage
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

if solve_sudoku(grid):
    # Display the solved grid
    for row in grid:
        print(" ".join(map(str, row)))
else:
    print("No solution exists.")
