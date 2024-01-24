# Maze, the final boss 

import sys

def parse_maze(filename):
    try:
        with open(filename, 'r') as file:
            first_line = file.readline().strip()
            lines = file.readlines()

        allowed_chars = set(first_line)
        maze = [list(line.strip()) for line in lines]
        start = exit = None
        rows, cols = len(maze), len(maze[0])

        for i, row in enumerate(maze):
            if len(row) != cols:
                raise ValueError("Every lines are not the same lenght or the maze isn't properly closed with '*'.")

        for i, row in enumerate(maze):
                for j, char in enumerate(row):
                    if char not in allowed_chars:
                        raise ValueError(f"Invalid character '{char}' in the maze.")
                    if char == '1':
                        start = (i, j)
                    elif char == '2':
                        exit = (i, j)

        return maze, start, exit, first_line
    except Exception as e:
        print(f"Error reading or parsing the maze file: {e}")
        sys.exit(1)

def print_maze(maze):
    for row in maze:
        print(''.join(row))

def find_shortest_path(maze, start, exit, wall_char):
    if not start or not exit:
        return None

    rows, cols = len(maze), len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = [(start, 0, [])]

    while queue:
        (x, y), steps, path = queue.pop(0)
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

def main():
    if len(sys.argv) != 2:
        print("Usage: python file_name.py labyrinth_path")
        sys.exit(1)

    try:
        labyrinth_path = sys.argv[1]
        maze, start, exit, first_line = parse_maze(labyrinth_path)
        wall_char = '*'  
        shortest_path = find_shortest_path(maze, start, exit, wall_char)

        if shortest_path:
            for x, y in shortest_path:
                if maze[x][y] not in ['1', '2']:
                    maze[x][y] = 'o'
            print(first_line)
            print_maze(maze)
            print(f"=> SORTIE ATTEINTE EN {len(shortest_path) - 1} COUPS !")
        else:
            print("Aucun chemin trouvé.")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

main()