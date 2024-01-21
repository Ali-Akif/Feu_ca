# Find shape

import sys

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            matrix = [[n for n in line.strip("\n")] for line in file]
            if not all(len(row) == len(matrix[0]) for row in matrix):
                raise ValueError("Lines in files must all be the same lenght.")
            return matrix
    except FileNotFoundError or ValueError or Exception or PermissionError:
        print("Error in file opening.")
        sys.exit(1)


def find_pattern(board, pattern):
    for board_line in range(len(board)):
        for board_collumn in range(len(board[0])):
            match = all((board[board_line + pattern_line][board_collumn + pattern_collumn] == pattern[pattern_line][pattern_collumn] or pattern[pattern_line][pattern_collumn] == " ")
                     for pattern_line in range(len(pattern))
                     for pattern_collumn in range(len(pattern[0])))
            if match:
                return [board_collumn, board_line]
    return None

def main(board_path, pattern_path):
    board = read_file(board_path)
    pattern = read_file(pattern_path)
    result = find_pattern(board, pattern)
    
    if result:
        found_collumn, found_line = result
        print("Found !")
        print(f"Coordinates : {result[0]}, {result[1]}")
        for board_line in range(len(board)):
            line = []
            for board_collumn in range(len(board[0])):
                if found_line <= board_line < found_line + len(pattern) and found_collumn <= board_collumn < found_collumn + len(pattern[0]) and pattern[board_line - found_line][board_collumn - found_collumn] != ' ':
                    line.append(board[board_line][board_collumn])
                else:
                    line.append("-")
            print("".join(line))
                
    else:
        print("Not found")

if len(sys.argv) != 3:
    print("use: python file.py board_path pattern_path")
main(sys.argv[1], sys.argv[2])
            