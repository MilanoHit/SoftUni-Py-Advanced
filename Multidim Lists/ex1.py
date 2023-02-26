n = int(input())
matrix = []
for i in range(n):
    row = input().split(", ")
    matrix.append([int(element) for element in row])
diagonals = [matrix[i][i] for i in range(n)]
diagonals_2 = [matrix[i][n - i - 1] for i in range(n)]
print(f"Primary diagonal: ", end= "")
sum1 = 0
for i in range(n - 1):
    print(diagonals[i], end=", ")
    sum1 += diagonals[i]
sum1 += diagonals[n -1]
print(f"{diagonals[n - 1]}. Sum: {sum1}")
print(f"Secondary diagonal: ", end= "")
sum1 = 0
for i in range(n -1):
    print(diagonals_2[i], end=", ")
    sum1 += diagonals_2[i]
sum1 += diagonals_2[n -1]
print(f"{diagonals_2[n - 1]}. Sum: {sum1}")
