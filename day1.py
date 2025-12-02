# AoC 2025-12-01 (Day 1)

with open("inputs/1.txt") as file:
    lines = [line.rstrip() for line in file]

position = 50
zerocount = 0
print("starting...")

def spin(direction, distance):
    global zerocount
    global position
    direction_int = 1
    if direction == "L":
        direction_int = -1

    for click in range(distance):
        position += direction_int
        position = position % 100
        if position == 0:
            zerocount += 1



for line in lines:
    if line == "":
        continue # Skip empty lines
    distance = line.strip("LR") # remove L and R
    print("line: " + line)
    print("distance: " + distance)
    distance = int(distance)

    spin(line[0], distance)

    


print("FINISHED: " + str(zerocount))



