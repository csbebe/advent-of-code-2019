import re

file = open("./Day_03/advent_3_input.txt", "r").read().splitlines()

wire_1 = file[0].split(',')
wire_2 = file[1].split(',')

def collect_coords(wire):
    x = 0
    y = 0
    path = []

    for step in wire:
        direction = step[0]
        distance = int(step[1:])

        if direction == 'U':
            for i in range(distance):
                y += 1
                path.append([x,y])
        elif direction == 'D':
            for i in range(distance):
                y -= 1
                path.append([x,y])
        elif direction == 'L':
            for i in range(distance):
                x -= 1
                path.append([x,y])
        elif direction == 'R':
            for i in range(distance):
                x += 1
                path.append([x,y])

    return path

def find_intersections(path_1, path_2):
    return list(map(list, set(map(tuple, path_1)) & set(map(tuple, path_2))))

def manhattan(x):
  return abs(x[0]) + abs(x[1])

path_1 = collect_coords(wire_1)
path_2 = collect_coords(wire_2)

closest = min([manhattan(x) for x in intersections])
print(closest)
