import math

file = open("./Day_01/advent_1_input.txt", "r")

result = 0
for line in file:
    while int(line) > 0:
        line = math.floor(int(line) / 3) - 2
        if line < 1:
            break;
        else:
            result += line
            
print(result)
