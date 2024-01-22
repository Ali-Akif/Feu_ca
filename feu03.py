# Sudoku

import sys

import sys

def main(file_path):
    sudoku = read_sudoku(file_path)
    if solve_sudoku(sudoku):
        print_sudoku(sudoku)
    else:
        print("No solutions")

def read_sudoku(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                for char in line.strip():
                    if char != "." and not char.isdigit():
                        raise ValueError("Error in the sudoku format, must be numbers and 0 or '.' for missing value.")
        with open(file_path, 'r') as file:
            sudoku = [[int(num) if num != "." else 0 for num in line.strip()] for line in file]

        if len(sudoku) != 9 or not all(len(row) == 9 for row in sudoku):
            raise ValueError("Format of sudoku must be 9x9.")
    except (FileNotFoundError, ValueError, PermissionError) as error:
        print(error)
        sys.exit(1)
    
    return sudoku

def is_valid(sudoku, row, col, num):
    if num in sudoku[row] or num in [sudoku[i][col] for i in range(9)]:
        return False
    start_row, start_col = 3 * ( row // 3 ), 3 * ( col // 3 )
    for i in range (start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if sudoku[i][j] == num:
                return False
    return True

def find_empty(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return i, j
    return False

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

def print_sudoku(sudoku):
    for row in sudoku:
        print("".join(str(num) for num in row))

if len(sys.argv) != 2:
    print("Use : python file_name file_path")
else:
    main(sys.argv[1])