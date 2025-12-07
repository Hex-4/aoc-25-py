# AoC 06/12/2025
import time
import re 
import copy

solution = 0
start_time = time.time()

with open("inputs/6.txt") as file:
    lines = [line.rstrip() for line in file]

operations_str = lines.pop()

nbr_lines = []

for line in lines:
    print(line)
    match = re.findall("\\d+", line)
    print(match)
    nbr_lines.append(match)

match = re.findall("[+*]", operations_str)
operations = match

lines_amount = len(nbr_lines)

for problem_idx, o in enumerate(operations):
    if o == "+":
        answer = 0
    elif o == "*":
        answer = 1

    for offset in range(lines_amount):
        if o == "+":
            answer += int(nbr_lines[offset][problem_idx])
        elif o == "*":
            answer *= int(nbr_lines[offset][problem_idx])
    solution += answer

print("SOLUTION: " + str(solution))

print("SOLUTION TOOK: " + str(time.time() - start_time))
