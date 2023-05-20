def is_valid(grid, row, col, num):
    # Check if the number already exists in the same row
    for i in range(9):
        if grid[row][i] == num:
            return False

    # Check if the number already exists in the same column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check if the number already exists in the same 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0  # Backtrack

                return False

    return True


def display_sudoku(grid):
    for row in range(9):
        for col in range(9):
            print(grid[row][col], end=" ")
            if col == 2 or col == 5:
                print("|", end=" ")
        print()
        if row == 2 or row == 5:
            print("-" * 21)

# Example puzzle
puzzle = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]

solve_sudoku(puzzle)
display_sudoku(puzzle)