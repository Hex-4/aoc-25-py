# AoC 05/12/2025
import time
import re 
import copy

solution = 0
start_time = time.time()

with open("inputs/5.txt") as file:
    lines = [line.rstrip() for line in file]



print("SOLUTION: " + str(solution))

print("SOLUTION TOOK: " + str(time.time() - start_time))
