import math

file = open("./Day_01/advent_1_input.txt", "r")

result = 0
for line in file:
    result += math.floor(int(line) / 3) - 2

print(result)
