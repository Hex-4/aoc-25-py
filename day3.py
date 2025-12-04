# AoC 02/12/2025
import time
import re 

solution = 0
start = time.time()

with open("inputs/3.txt") as file:
    lines = [line.rstrip() for line in file]

def find_bit(line: str, digit: str):
    if digit in line:
        i = line.index(digit)
        if i + 1 == len(line):
            return
        return line[i:]
    return

def solve_last_bit(line: str):
    for digit in reversed(range(1,10)):
        if not str(digit) in line[1:]:
            continue
        return int(line[0] + str(digit))
    return

for line in lines:
    print(line)

    for digit in reversed(range(1,10)): # 1-9
        next_bit = find_bit(line, str(digit))
        if next_bit:
            joltage = solve_last_bit(next_bit)
            if joltage:
                solution += joltage
                print(joltage)
                break


print("SOLUTION: " + str(solution))

print("SOLUTION TOOK: " + str(time.time() - start))
