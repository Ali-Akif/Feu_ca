# Sudoku

import sys

def read_sudoku(file_path):
    with open(file_path, 'r') as file:
        for row in file:
            for char in row.strip():
                if char != "." and not char.isdigit():
                    print("Error in sudoku format")
                    sys.exit(1)

    with open(file_path, 'r') as file:
        sudoku = [[int(num) if num != '.' else 0 for num in line.strip()] for line in file]

    if len(sudoku) != 9 or not all(len(row) == 9 for row in sudoku):
        print("Error: Sudoku grid should be 9x9")
        sys.exit(1)
    return sudoku

def is_valid(sudoku, row, col, num):
    if num in sudoku[row]:
        return False
    if num in [sudoku[i][col] for i in range(9)]:
        return False
    startRow, startCol = 3 * (row // 3), 3 * (col // 3)
    for i in range(startRow, startRow + 3):
        for j in range(startCol, startCol + 3):
            if sudoku[i][j] == num:
                return False
    return True

def solve_sudoku(sudoku):
    empty = find_empty(sudoku) 
    if not empty:
        return True
    row, col = empty 
    for num in range(1, 10):
        if is_valid(sudoku, row, col, num):
            sudoku[row][col] = num
            if solve_sudoku(sudoku):
                return True
            sudoku[row][col] = 0
    return False

def find_empty(sudoku):
    for i in range(9): 
        for j in range(9): 
            if sudoku[i][j] == 0:
                return i, j
    return None

def print_sudoku(sudoku):
    for row in sudoku:
        print("".join(str(num) for num in row))

def main(file_path):
    sudoku = read_sudoku(file_path)
    if solve_sudoku(sudoku):
        print_sudoku(sudoku)
    else:
        print("Pas de solution")

if len(sys.argv) > 1:
    main(sys.argv[1])
else:
    print("Usage: python sudoku_solver.py [file path]")