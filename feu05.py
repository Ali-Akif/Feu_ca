import sys

def parse_maze(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    maze = [list(line.strip()) for line in lines]
    start = exit = None
    for i, row in enumerate(maze):
        for j, char in enumerate(row):
            if char == '1':  # Start character
                start = (i, j)
            elif char == '2':  # End character
                exit = (i, j)

    return maze, start, exit

def print_maze(maze):
    for row in maze:
        print(''.join(row))

def find_shortest_path(maze, start, exit, wall_char):
    if not start or not exit:
        return None

    rows, cols = len(maze), len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = [(start, 0, [])]  # Using a list as a queue

    while queue:
        (x, y), steps, path = queue.pop(0)  # Pop from the start of the list
        if (x, y) == exit:
            return path + [(x, y)]
        if visited[x][y] or maze[x][y] == wall_char:
            continue
        visited[x][y] = True
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < rows and 0 <= new_y < cols and not visited[new_x][new_y]:
                queue.append(((new_x, new_y), steps + 1, path + [(x, y)]))

    return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python file_name.py labyrinth_path")
        sys.exit(1)

    labyrinth_path = sys.argv[1]
    maze, start, exit = parse_maze(labyrinth_path)
    wall_char = '*'  # Define the wall character

    shortest_path = find_shortest_path(maze, start, exit, wall_char)

    if shortest_path:
        for y, x in shortest_path:
            if maze[y][x] not in ['1', '2']:
                maze[y][x] = 'o'
        print_maze(maze)
        print(f"=> SORTIE ATTEINTE EN {len(shortest_path) - 1} COUPS !")
    else:
        print("Aucun chemin trouvé.")
