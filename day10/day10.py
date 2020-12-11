file = open("day10.txt").read().split("\n")
jolts = [int(num) for num in file if num]
jolts.sort()
od = 1
td = 1
# Part 1
for i in range(1, len(jolts)):
    diff = jolts[i] - jolts[i-1]
    if diff == 1:
        od += 1
    elif diff == 3:
        td += 1
print(od * td)

# Part 2
# Didn't want to think up a better solution
# so this would work, but take more than an hour


def comb(start):
    tot = 0
    if start + 1 > jolts[len(jolts)-1]:
        return 1
    if (start + 1) in jolts:
        tot += comb(start + 1)
    if (start + 2) in jolts:
        tot += comb(start + 2)
    if (start + 3) in jolts:
        tot += comb(start + 3)
    return tot


print(comb(0))
