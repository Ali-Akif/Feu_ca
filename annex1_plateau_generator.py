import sys
import random

def generate_plateau(width, height, density):
    plateau = f"{height}.xo\n"
    for _ in range(height):
        line = ''.join('x' if random.randint(0, height * 2) < density else '.' for _ in range(width))
        plateau += line + '\n'
    return plateau

if len(sys.argv) != 4:
    print("Usage: python generate_plateau.py width height density")
    sys.exit(1)

width = int(sys.argv[1])
height = int(sys.argv[2])
density = int(sys.argv[3])

a = generate_plateau(width, height, density)
print(a)
