def init():
    file = open("./Day_02/advent_2_input.txt", "r").read().split(',')

    for i in range(0, len(file)):
        file[i] = int(file[i])

    return file

def run(noun, verb, data):
    data[1] = noun
    data[2] = verb

    for i in range(0, len(data), 4):
        if data[i] == 99:
            break

        x = data[i + 1]
        y = data[i + 2]
        ind = data[i + 3]

        if data[i] == 1:
            data[ind] = data[x] + data[y]
        elif data[i] == 2:
            data[ind] = data[x] * data[y]

    return data[0]

for i in range(99):
    for j in range(99):
        data = init()
        if run(i, j, data) == 19690720:
            print(100 * i + j)
            break
