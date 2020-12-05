import math

file = open("day5.txt").read().split("\n")
max = 0
# Part 1
allseats = []
for seat in file:
    pos = [0, 127]
    col = [0, 7]
    seats = 128
    cols = 8
    for char in seat[0:7]:
        seats /= 2
        if char == "F":
            pos[1] -= seats
        else:
            pos[0] += seats
    for char in seat[7:]:
        cols /= 2
        if char == "L":
            col[1] -= cols
        else:
            col[0] += cols
    if (pos[1] * 8 + col[1]) >= max:
        max = (pos[1] * 8 + col[1])
# Part 2
    allseats.append((pos[1] * 8 + col[1]))
print(max)
allseats.sort()
myseat = allseats[0]
for n in range(len(allseats)):
    if myseat == allseats[n] - 1:
        print(myseat)
        break
    myseat += 1
