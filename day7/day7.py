file = open("day7.txt").read().split("\n")
bags = {}
lbags = {}
gbags = set()

# Part 1


def checkBag(line):
    if line == "shiny gold bag":
        return True
    elif line == " other bag":
        return False
    for bag in bags[line]:
        if checkBag(bag):
            gbags.add(line)
            return True


# Part 2
def checkLen(bag):
    total = 1
    for n, b in lbags[bag]:
        total += n * checkLen(b)
    return total


for line in file:
    l = line.split("s contain")
    b = l[1].split(",")
    temp = []
    templ = []
    for bag in b:
        temp.append(bag[3:].rstrip("s."))
        if bag[1].isdigit():
            templ.append((int(bag[1]), bag[3:].rstrip("s.")))
    bags[l[0]] = temp
    lbags[l[0]] = templ
for line in file:
    l = line.split("s contain")
    checkBag(l[0])
print(checkLen("shiny gold bag") - 1)
print(len(gbags))
