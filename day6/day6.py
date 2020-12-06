file = open("day6.txt").read().split("\n\n")
total1 = 0
total2 = 0
# Part 1
for line in file:
    l = line.replace("\n", "")
    chars = set(())
    for char in l:
        chars.add(char)
    total1 += len(chars)
# Part 2
    l = line.split("\n")
    for char in l[0]:
        gc = 0
        for p in range(len(l)-1):
            if char in l[p+1]:
                gc += 1
        if gc + 1 == len(l):
            total2 += 1
print(total1)
print(total2)
