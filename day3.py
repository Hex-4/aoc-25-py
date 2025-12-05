# AoC 03/12/2025
import time
import re 

solution = 0
start = time.time()

with open("inputs/3.txt") as file:
    lines = [line.rstrip() for line in file]


            


for line in lines:
    budget = len(line) - 12
    
    stack = []

    for digit in line:
        while stack and budget > 0 and int(stack[-1]) < int(digit):
            stack.pop()
            budget -= 1
        stack.append(digit)

    stack = stack[:12]
    joltage = int("".join(stack))

    solution +=joltage
print("SOLUTION: " + str(solution))

print("SOLUTION TOOK: " + str(time.time() - start))
