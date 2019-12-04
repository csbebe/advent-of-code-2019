file = open("./Day_02/advent_2_input.txt", "r").read().split(',')

for i in range(0, len(file)):
    file[i] = int(file[i])

file[1] = 12
file[2] = 2

for i in range(0, len(file), 4):
    if file[i] == 99:
        break

    x = file[i + 1]
    y = file[i + 2]
    ind = file[i + 3]

    if file[i] == 1:
        file[ind] = file[x] + file[y]
    elif file[i] == 2:
        file[ind] = file[x] * file[y]

print(file[0])
