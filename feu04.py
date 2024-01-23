import sys

def read_plateau(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]
    if not lines or not lines[0]:
        raise ValueError("Empty plateau file.")

    empty, obstacle, full = '.', 'x', 'o'
    valid_chars = (empty, obstacle)
    reference_length = len(lines[0])

    if not all(len(line) == reference_length for line in lines):
        raise ValueError
    if not all(char in valid_chars for row in lines for char in row):
        raise ValueError
    return [list(line) for line in lines], empty, obstacle, full

def find_largest_square(plateau, empty, obstacle):
    height, width = len(plateau), len(plateau[0])
    max_square = [[0] * width for _ in range(height)]
    max_size, max_pos = 0, (0, 0)

    for i in range(height):
        for j in range(width):
            if plateau[i][j] == empty:
                if i > 0 and j > 0:
                    left = max_square[i][j - 1]
                    top = max_square[i - 1][j]
                    top_left = max_square[i - 1][j - 1]

                    smallest = left
                    if top < smallest:
                        smallest = top
                    if top_left < smallest:
                        smallest = top_left

                    max_square[i][j] = 1 + smallest
                else:
                    max_square[i][j] = 1
                    
                if max_square[i][j] > max_size:
                    max_size = max_square[i][j]
                    max_pos = (i, j)

    return max_size, max_pos

def fill_largest_square(plateau, max_size, max_pos, full):
    for i in range(max_pos[0] - max_size + 1, max_pos[0] + 1):
        for j in range(max_pos[1] - max_size + 1, max_pos[1] + 1):
            plateau[i][j] = full
    return plateau

def display_plateau(plateau):
    for line in plateau:
        print(''.join(line))


if len(sys.argv) != 2:
    print("Use: python feu04.py path_to_plateau_file")
    sys.exit(1)

try:
    plateau, empty, obstacle, full = read_plateau(sys.argv[1])
    max_size, max_pos = find_largest_square(plateau, empty, obstacle)
    filled_plateau = fill_largest_square(plateau, max_size, max_pos, full)
    display_plateau(filled_plateau)
except (ValueError, FileNotFoundError, Exception):
    print("An error occured while reading your plateau.")
    sys.exit(1)
