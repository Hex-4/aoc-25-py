# AoC 04/12/2025
import time
import re 
import copy

solution = 0
start = time.time()

with open("inputs/4.txt") as file:
    lines = [line.rstrip() for line in file]

grid = []

for line in lines:
    line_rolls = []
    for char in line:
        if char == ".":
            line_rolls.append(False)
        elif char == "@":
            line_rolls.append(True)
        else:
            raise ValueError("found an invalid character!")
    grid.append(line_rolls)

def check_neighbors(x: int, y: int):
    global grid
    global removed_grid
    neighbors = 0
    for y_off in range(-1, 2): # -1, 0, 1
        for x_off in range(-1, 2):
            try:
                if y + y_off < 0:
                    neighbors += 0
                elif x + x_off < 0:
                    neighbors += 0
                elif grid[y + y_off][x + x_off]:
                    neighbors += 1
            except IndexError:
                neighbors += 0

    neighbors -= 1

    if neighbors < 4:
        removed_grid[y][x] = False
        return True
    else:
        return False


removed_grid = []

while removed_grid != grid:
    if removed_grid == []:
        removed_grid = copy.deepcopy(grid)
    else:
        grid= copy.deepcopy(removed_grid)
    for y, line in enumerate(grid):

        for x, roll in enumerate(line):
            if roll:
                if check_neighbors(x, y):
                    solution += 1





print("SOLUTION: " + str(solution))

print("SOLUTION TOOK: " + str(time.time() - start))
