arr = [[], [], []]

def printBoard(arr):
    print(f"| {arr[0][0]} | {arr[0][1]} | {arr[0][2]} |")
    print(f"| {arr[1][0]} | {arr[1][1]} | {arr[1][2]} |")
    print(f"| {arr[2][0]} | {arr[2][1]} | {arr[2][2]} |")


def CheckforWin(arr, playerX, player0) -> bool:

    for i in range(len(arr)):

        take_first = arr[i][0]
        if arr[i][1] == take_first and arr[i][2] == take_first and take_first != " ":
            if take_first == "X":
                print(f"Congratulations, {playerX} won!")
                return True
            elif take_first == "O":
                print(f"Congratulations, {player0} won!")
                return True

        take_two = arr[0][i]
        if arr[1][i] == take_two and arr[2][i] == take_two and take_two != " ":
            if take_two == "X":
                print(f"Congratulations, {playerX} won!")
                return True
            elif take_two == "O":
                print(f"Congratulations, {player0} won!")
                return True

    if arr[0][0] == arr[1][1] == arr[2][2]:
        if arr[0][0] == "X":
            print(f"Congratulations, {playerX} won!")
            return True
        elif arr[0][0] == "O":
            print(f"Congratulations, {player0} won!")
            return True
    if arr[2][0] == arr[1][1] == arr[0][2]:
        if arr[2][0] == "X":
            print(f"Congratulations, {playerX} won!")
            return True
        elif arr[2][0] == "O":
            print(f"Congratulations, {player0} won!")
            return True

def makeBoard(arr):
    for i in range(3):

        for p in range(3):
            arr[i].append(" ")

makeBoard(arr)
player1 = ""
player2 = ""
print("Enter first player name: ")
name1 = input()
print("Enter second player name: ")
name2 = input()
print(f"Player {name1} X or O")
choice = input()
if choice == "X":
    player1 = name1
    player2 = name2
else:
    player1 = name2
    player2 = name1
count = 0
while True:
    if count%2 == 0:
        print(f"{player1}"'s turn')
        choice = input()
        arr[(int(choice) - 1)//3][int(choice) % 3 - 1] = "X"
    elif count%2 == 1:
        print(f"{player2}"'s turn')
        choice = input()
        arr[(int(choice) - 1)//3][int(choice) % 3 - 1] = "O"
    if CheckforWin(arr, player1, player2):
        printBoard(arr)
        break
    printBoard(arr)
    count += 1


