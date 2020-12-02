file = open("day2.txt", "r")
count = 0
text = file.readline()
big1 = 0
big2 = 0
while text != "":
    if text != "":
        num = text.split("-")
        less = int(num[0])
        most = int(num[1][:2])
        space = text.split(" ")
        letter = space[1][0]
        count = 0
# Part 1
        for char in space[2]:
            if char == letter:
                count += 1
        if count <= most and count >= less:
            big1 += 1
# Part 2
        if (letter == space[2][less-1] and letter != space[2][most-1]) or (letter != space[2][less-1] and letter == space[2][most-1]):
            big2 += 1
        text = file.readline()
print(big1)
print(big2)
