file = open("day8.txt").read().split("\n")
total = 0
i = 0
term = len(file)
visited = []
b = True
# Part 1
while b:
    line = file[i]
    for num in visited:
        if i == num:
            b = False
    visited.append(i)
    if not b:
        break
    if line[:3] == "acc":
        total += int(line[4:])
        i += 1
    elif line[:3] == "jmp":
        i += int(line[4:])
    else:
        i += 1
print(total)

# Part 2
for l in range(term):
    nfile = [line.split(" ") for line in file if line]
    if file[l][:3] == "nop":
        nfile[l][0] = "jmp"
    elif file[l][:3] == "jmp":
        nfile[l][0] = "nop"
    total = 0
    i = 0
    visited = set()
    while i < term:
        nline = nfile[i]
        if i in visited:
            break
        visited.add(i)
        if nline[0] == "acc":
            total += int(nline[1])
            i += 1
        elif nline[0] == "jmp":
            i += int(nline[1])
        else:
            i += 1
    if i >= term:
        print(total)
