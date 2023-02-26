colors = input().split()
filtered_colors = []

while len(colors) > 0:
    if "red" == colors[0] + colors[len(colors) - 1] or "red" == colors[len(colors) - 1] + colors[0]:
        filtered_colors.append("red")
        colors.pop(0)
        if len(colors) > 0:
            colors.pop(len(colors) - 1)

    elif "blue" == colors[0] + colors[len(colors) - 1] or "blue" == colors[len(colors) - 1] + colors[0]:
        filtered_colors.append("blue")
        colors.pop(0)
        if len(colors) > 0:
            colors.pop(len(colors) - 1)

    elif "yellow" == colors[0] + colors[len(colors) - 1] or "yellow" == colors[len(colors) - 1] + colors[0]:
        filtered_colors.append("yellow")
        colors.pop(0)
        if len(colors) > 0:
            colors.pop(len(colors) - 1)

    elif "orange" == colors[0] + colors[len(colors) - 1] or "orange" == colors[len(colors) - 1] + colors[0]:
        filtered_colors.append("orange")
        colors.pop(0)
        if len(colors) > 0:
            colors.pop(len(colors) - 1)

    elif "purple" == colors[0] + colors[len(colors) - 1] or "purple" == colors[len(colors) - 1] + colors[0]:
        filtered_colors.append("purple")
        colors.pop(0)
        if len(colors) > 0:
            colors.pop(len(colors) - 1)

    elif "green" == colors[0] + colors[len(colors) - 1] or "green" == colors[len(colors) - 1] + colors[0]:
        filtered_colors.append("green")
        colors.pop(0)
        if len(colors) > 0:
            colors.pop(len(colors) - 1)
    else:
        if len(colors) % 2 == 0:
            if colors[0][1:] != "" or colors[len(colors) - 1][:-1] != "":
                colors.insert(int(len(colors) / 2), colors[0][1:])
                colors.insert(int((len(colors) + 1) / 2), colors[len(colors) - 1][:-1])
            colors.pop(0)
            colors.pop(len(colors) - 1)
        elif len(colors) > 1:
            if colors[0][1:] != "" or colors[len(colors) - 1][:-1] != "":
                colors.insert(int((len(colors) + 1) / 2), colors[0][1:])
                colors.insert(int((len(colors)) / 2), colors[len(colors) - 1][:-1])
            colors.pop(0)
            colors.pop(len(colors) - 1)
        else:
            break

for i in range(len(filtered_colors)):
    if filtered_colors[i] == "purple":
        if "red" not in filtered_colors or "blue" not in filtered_colors:
            filtered_colors.pop(i)
    elif filtered_colors[i] == "orange":
        if "red" not in filtered_colors or "yellow" not in filtered_colors:
            filtered_colors.pop(i)
    elif filtered_colors[i] == "green":
        if "blue" not in filtered_colors or "yellow" not in filtered_colors:
            filtered_colors.pop(i)

print(filtered_colors)