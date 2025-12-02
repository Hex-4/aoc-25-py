# AoC 2025-12-01 (Day 1)

with open("inputs/1.txt") as file:
    lines = [line.rstrip() for line in file]

position = 50
zerocount = 0
print("starting...")

def spin(direction, distance):
    global position
    if direction == "L":
        position -= distance
        print("spinning left " + str(distance))
    elif direction == "R":
        position += distance
        print("spinning right " + str(distance))

    position = position % 100

for line in lines:
    if line == "":
        continue # Skip empty lines
    distance = line.strip("LR") # remove L and R
    print("line: " + line)
    print("distance: " + distance)
    distance = int(distance)

    spin(line[0], distance)

    if position == 0:
        zerocount += 1


print("FINISHED: " + str(zerocount))



