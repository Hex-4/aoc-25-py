# AoC 02/12/2025
import time
import re 

start = time.time()

with open("inputs/2.txt") as file:
    rangestrings = file.readline().split(",")

ranges = []
solution = 0

for r in rangestrings:
    ranges.append(r.split("-", 1))

for r in ranges:
    for n in range(int(r[0]), int(r[1]) + 1):
        match = re.search("^(\\d+?)\\1+$", str(n))
        if match:
            if match.group() == str(n):
                solution += n
        
print(solution)
print(time.time() - start)

