import re

file = open("./Day_03/advent_3_input.txt", "r").read().splitlines()

wire_1 = file[0].split(',')
wire_2 = file[1].split(',')

def collect_coords(wire):
    x = 0
    y = 0
    cntr = 0
    path = dict()

    for step in wire:
        direction = step[0]
        distance = int(step[1:])

        if direction == 'U':
            for i in range(distance):
                y += 1
                cntr += 1
                path[(x, y)] = cntr
        elif direction == 'D':
            for i in range(distance):
                y -= 1
                cntr += 1
                path[(x, y)] = cntr
        elif direction == 'L':
            for i in range(distance):
                x -= 1
                cntr += 1
                path[(x, y)] = cntr
        elif direction == 'R':
            for i in range(distance):
                x += 1
                cntr += 1
                path[(x, y)] = cntr

    return path

def find_intersections(path_1, path_2):
    intersections = dict()
    for coord in path_1.keys():
        if coord in path_2:
            intersections[coord] = path_1[coord] + path_2[coord]

    return intersections

path_1 = collect_coords(wire_1)
path_2 = collect_coords(wire_2)

intersections = find_intersections(path_1, path_2)

min = min(intersections.keys(), key=(lambda k: intersections[k]))
print(intersections[min])
