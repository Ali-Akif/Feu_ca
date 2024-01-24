import random

def generate_maze(height, width, wall_char, path_char, start_char, end_char):
    maze = []
    entry = random.randint(2, width - 3)
    exit = random.randint(2, width - 3)

    for y in range(height):
        row = ""
        for x in range(width):
            if y == height - 1 and x == entry:
                row += start_char
            elif y == 0 and x == exit:
                row += end_char
            elif 1 <= y < height - 1 and 1 <= x < width - 1 and random.randint(0, 99) > 205 :
                row += path_char
            else:
                row += wall_char
        maze.append(row)
    return maze

height = int(input("Entrez la hauteur du labyrinthe: "))
width = int(input("Entrez la largeur du labyrinthe: "))
wall_char, path_char, start_char, end_char, full_char = "*", " ", "1", "2", "o"
maze = generate_maze(height, width, wall_char, path_char, start_char, end_char)


print(f"{height}x{width}{wall_char}{path_char}{full_char}{start_char}{end_char}")
for row in maze:
    print(row)