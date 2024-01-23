import random

def generate_maze(height, width, wall_char, path_char, start_char, end_char):
    maze = []
    entry = random.randint(2, width - 3)
    exit = random.randint(2, width - 3)

    for y in range(height):
        row = ""
        for x in range(width):
            if y == height - 1 and x == entry:
                row += start_char  # Départ
            elif y == 0 and x == exit:
                row += end_char  # Arrivée
            elif 1 <= y < height - 1 and 1 <= x < width - 1 and random.randint(0, 99) > 20:
                row += path_char  # Case vide
            else:
                row += wall_char  # Obstacle
        maze.append(row)

    return maze

# Fonction pour vérifier si l'entrée est un seul caractère
def is_single_char(input_str):
    return len(input_str) == 1

# Demander les informations du labyrinthe
try:
    height = int(input("Entrez la hauteur du labyrinthe: "))
    width = int(input("Entrez la largeur du labyrinthe: "))
    wall_char = input("Caractère pour les obstacles: ")
    path_char = input("Caractère pour les cases vides: ")
    start_char = input("Caractère pour le départ: ")
    end_char = input("Caractère pour l'arrivée: ")

    if not all(is_single_char(c) for c in [wall_char, path_char, start_char, end_char]):
        raise ValueError("Chaque caractère doit être unique et individuel.")

    maze = generate_maze(height, width, wall_char, path_char, start_char, end_char)

    # Affichage du labyrinthe
    for row in maze:
        print(row)

except ValueError as e:
    print(f"Erreur : {e}")
