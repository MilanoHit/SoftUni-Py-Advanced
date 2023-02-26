import os
path = input()


files = os.listdir(path)
for i in range(len(files)):
    files[i] = files[i].split(".")

exten = files[0][1]
print(exten)
for i in range(len(files)):
    if files[i][1] == exten:
        print(f"---{files[i][0]}.{files[i][1]}")
    else:
        exten = files[i][1]
        print(exten)
        print(f"---{files[i][0]}.{files[i][1]}")