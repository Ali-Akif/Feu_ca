# WARMUP

import sys

# Part 1 : function

def rectangle_printer(width, height):
    top_and_bottom = "o" + "-" * (width - 2) + "o" if width > 1 else "o"
    middle = "|" + " " * (width - 2) + "|" if width > 1 else "|" 

    for i in range(lenght):
        if i == 0 or i == lenght - 1:
            print(top_and_bottom)
        else:
            print(middle)


# Part 2 : Error Handling and slicing

if len(sys.argv) != 3 or not "".join(sys.argv[1:]).isdigit() or "0" in sys.argv[1:]:
    print("error")
    sys.exit(1)
else:
    width, lenght = int(sys.argv[1]), int(sys.argv[2])


# Part 3 : Resolution and display

rectangle_printer(width, lenght)