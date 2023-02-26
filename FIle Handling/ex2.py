file = open("text.txt", "r")
symbols = [",", "!", ".", "'", "?"]
lines = []
file2 = open("output.txt", "w")
for line in file:
    lines.append(line)

for i in range(len(lines)):
    characters = 0
    punct = 0

    for p in range(len(lines[i])):
        if lines[i][p] in symbols:
            punct += 1
        elif lines[i][p] != " " and lines[i][p] != "\n":
            characters += 1
    line = "Line: "
    line += f"{i + 1}"
    line += " " + lines[i][:-1]
    line += f" ({characters}) " + f"({punct})"
    file2.write(line)
    file2.write("\n")
file.close()
file2.close()

