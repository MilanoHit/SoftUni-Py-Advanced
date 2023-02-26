file = open("text.txt", "r")
symbols = ["-", ",", ".", "!", "?"]
lines = []

for line in file:
    lines.append(line)
for i in range(len(lines)):
    line = lines[i]
    line2 = ''
    for p in range(0, len(line)):
        if line[p] in symbols:
            line2 += line2.join("@")
        elif line[p] == "\n":
            continue
        else:
            line2 += line2.join(line[p])
    line2 = line2.split(" ")
    for p in range(len(line2)):
        if p != len(line2) - 1:
            print(line2[p][::-1], end = " ")
        else:
            print(line2[p][::-1])

file.close()