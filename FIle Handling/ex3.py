import os
command = input().split("-")

while command[0] != "End":

    if command[0] == "Create":
        file = open(command[1], "w")
        file.close()
    elif command[0] == "Add":
        file = open(command[1], "a")
        file.write(command[2])
        file.close()
    elif command[0] == "Replace":
        try:
            file = open(command[1], "r")
            lines = []
            for line in file:
                lines.append(line)
            for i in range(len(lines)):
                if command[2] in lines[i]:
                    lines[i] = lines[i].replace(command[2], command[3])
            file.close()
            file = open(command[1], "w")
            for i in range(len(lines)):
                file.write(lines[i])
            file.close()
        except FileNotFoundError as e:
            print(e)

    elif command[0] == "Delete":
        try:
            os.remove(command[1])
        except FileNotFoundError as e:
            print(e)
    command = input().split("-")