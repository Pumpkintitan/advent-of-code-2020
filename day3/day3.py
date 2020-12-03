file = open("day3.txt").read().split("\n")


def slope(x, y):
    tc = 0
    s = x
    sy = y
    while sy < len(file):
        if file[sy][s % len(file[0])] == "#":
            tc += 1
        s += x
        sy += y
    return tc


print(slope(1, 1)*slope(3, 1)*slope(5, 1)*slope(7, 1)*slope(1, 2))
