n = int(input())
matrix = []
for i in range(n):
    row = input().split()
    matrix.append([int(element) for element in row])
diagonals = [matrix[i][i] for i in range(n)]
diagonals_2 = [matrix[i][n - i - 1] for i in range(n)]
sum1 = 0
sum2 = 0
for i in range(n):
    sum1 += diagonals[i]
    sum2 += diagonals_2[i]
print(abs(sum1 - sum2))