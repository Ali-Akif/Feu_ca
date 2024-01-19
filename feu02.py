import sys

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return [list(line.strip('\n')) for line in file]
    except Exception as e:
        raise IOError(f"Erreur lors de la lecture du fichier '{file_path}': {e}")

def find_pattern(board, pattern):
    if not board or not pattern:
        return None

    for i in range(len(board) - len(pattern) + 1):
        for j in range(len(board[0]) - len(pattern[0]) + 1):
            match = all((board[i + x][j + y] == pattern[x][y] or pattern[x][y] == ' ')
                        for x in range(len(pattern))
                        for y in range(len(pattern[0])))
            if match:
                return j, i, match
    return None

def main(board_file, pattern_file):
    try:
        board = read_file(board_file)
        pattern = read_file(pattern_file)
    except IOError as e:
        print(e)
        return

    if len(board[0]) != len(pattern[0]) and len(board) != len(pattern):
        print("Erreur : Les dimensions du tableau et du motif ne correspondent pas.")
        return

    result = find_pattern(board, pattern)
    if result:
        print("Trouvé !")
        print(f"Coordonnées : {result[0]},{result[1]}")
    else:
        print("Introuvable")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Erreur : Nombre d'arguments insuffisant.")
        print("Utilisation : python script.py [chemin du fichier tableau] [chemin du fichier motif]")
    else:
        main(sys.argv[1], sys.argv[2])
