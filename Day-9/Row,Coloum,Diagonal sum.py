matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
rows = len(matrix)
cols = len(matrix[0])
row_s = [0]*rows
col_s = [0]*cols
diagonal_s = 0
for i in range(rows):
    for j in range (cols):
        row_s[i]+=matrix[i][j]
        col_s[j]+=matrix[i][j]
        if i == j:
            diagonal_s+=matrix[i][j]
print(row_s)
print(col_s)
print(diagonal_s)
