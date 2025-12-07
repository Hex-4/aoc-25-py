# AoC 05/12/2025
import time
import re 
import copy

solution = 0
start_time = time.time()

ranges = []

with open("inputs/5.txt") as file:
    lines = [line.rstrip() for line in file]

for line in lines:
    if line == "":
        continue
    elif "-" in line:
        match = re.match("(\\d+)-(\\d+)", line)

        start, end = match.groups()
        
        ranges.append((int(start), int(end)))

ranges.sort()

merged = [ranges[0]]

for start, end in ranges[1:]:
    last_start, last_end = merged[-1] # get last range
    
    if start <= last_end:
        merged[-1] = (last_start, max(end, last_end))
    else:
        merged.append((start,end))

print(merged)

for start, end in merged:
    solution += (end - start) + 1






print("SOLUTION: " + str(solution))

print("SOLUTION TOOK: " + str(time.time() - start_time))
