matrix = [
    [4, 5, 6],
    [10, 15, 2],
    [3, 8, 19]
]
print(matrix[0])
print(matrix[0][2])
matrix[2][1] = 0
print(matrix)
print(matrix[2][1])
for row in matrix:
    for item in row:
        print(item)