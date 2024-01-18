import sys

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        return [list(line.strip('\n')) for line in file]

def find_pattern(board, pattern):
    for i in range(len(board) - len(pattern) + 1):
        for j in range(len(board[0]) - len(pattern[0]) + 1):
            match = all((board[i + x][j + y] == pattern[x][y] or pattern[x][y] == ' ')
                        for x in range(len(pattern)) 
                        for y in range(len(pattern[0])))
            if match:
                return (j, i)
    return None

def main(board_file, pattern_file):
    board = read_data_from_file(board_file)
    pattern = read_data_from_file(pattern_file)
    result = find_pattern(board, pattern)
    if result:
        print("Trouvé !")
        print(f"Coordonnées : {result[0]},{result[1]}")
    else:
        print("Introuvable")

if len(sys.argv) != 3:
    print("Usage: python feu02.py [board file path] [pattern file path]")
else:
    main(sys.argv[1], sys.argv[2])


