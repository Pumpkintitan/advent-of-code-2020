file = open("day4.txt").read().split("\n")
valid = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
temp = []
total = 0

# Part 1


def check(temp):
    valcount = 0
    for field in temp:
        for val in valid:
            if field[:3] == val:
                valcount += 1
    if valcount == 7:
        return 1
    else:
        return 0

# Part2


valchar = ["0", "1", "2", "3", "4", "5", "6",
           "7", "8", "9", "a", "b", "c", "d", "e", "f"]
valeye = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def chackMore(temp):
    valcount = 0
    if check(temp) == 1:
        for field in temp:
            t = field.split(":")
            if t[0] == "byr":
                if len(t[1]) == 4 and 1920 <= int(t[1]) <= 2002:
                    valcount += 1
            elif t[0] == "iyr":
                if len(t[1]) == 4 and 2010 <= int(t[1]) <= 2020:
                    valcount += 1
            elif t[0] == "eyr":
                if len(t[1]) == 4 and 2020 <= int(t[1]) <= 2030:
                    valcount += 1
            elif t[0] == "hgt":
                if t[1][-2:] == "cm":
                    n = t[1].split("c")
                    if 150 <= int(n[0]) <= 193:
                        valcount += 1
                elif t[1][-2:] == "in":
                    n = t[1].split("i")
                    if 59 <= int(n[0]) <= 76:
                        valcount += 1
            elif t[0] == "hcl":
                if t[1][0] == "#" and len(t[1][1:]) == 6:
                    val = 0
                    for char in t[1][1:]:
                        for vchar in valchar:
                            if char == vchar:
                                val += 1
                    if val == 6:
                        valcount += 1
            elif t[0] == "ecl":
                for eye in valeye:
                    if eye == t[1]:
                        valcount += 1
                        break
            elif t[0] == "pid":
                if len(t[1]) == 9 and int(t[1]):
                    valcount += 1
    if valcount == 7:
        return 1
    else:
        return 0


for line in file:
    if line != "":
        for thing in line.split(" "):
            temp.append(thing)
    else:
        total += chackMore(temp)
        temp = []
total += chackMore(temp)
print(total)
