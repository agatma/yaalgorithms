n = int(input())
m = int(input())

matrix = [[int(value) for value in input().split()] for _ in range(n)]

for column in range(m):
    print(*[matrix[row][column] for row in range(n)])