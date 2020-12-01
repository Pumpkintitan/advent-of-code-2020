file = open("day1.txt", "r")
nums = []
text = 0
while text != "":
    text = file.readline()
    nums.append(text)
# Part 1
for numi in nums:
    for numj in nums:
        if numi != "" and numj != "":
            if (int(numi) + int(numj) == 2020):
                print(int(numi) * int(numj))
# Part 2
            for numk in nums:
                if numk != "":
                    if (int(numi) + int(numj) + int(numk) == 2020):
                        print(int(numi) * int(numj) * int(numk))
