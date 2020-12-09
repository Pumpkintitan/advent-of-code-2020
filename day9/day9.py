file = open("day9.txt").read().split("\n")
nums = []
inval = 0
for line in file:
    nums.append(int(line))
# Part 1
for i in range(25, len(nums)):
    target = nums[i]
    others = nums[i-25:i]
    found = False
    for other in others:
        if target - other in others:
            found = True
    if not found:
        inval = nums[i]
        print(nums[i])

# Part 2
found = False
for i in range(len(nums)):
    if found:
        break
    total = 0
    b = []
    for j in range(i, len(nums)):
        total += nums[j]
        b.append(nums[j])
        if total == inval:
            b.sort()
            print(b[0] + b[len(b) - 1])
            found = True
            break
        elif total > inval:
            break
