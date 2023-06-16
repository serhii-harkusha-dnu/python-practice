# Робота на GITHUB - https://github.com/serhii-harkusha-dnu/python-practice/tree/main
# Двовимірний масив
# Студента групи КМ-22-1
# Гаркуші Сергія

print("Enter 5x4 matrix:")
matrix = []
for i in range(0, 5):
    matrix.append(list(map(float, input().split()[0:4])))
    
rowSums = []
for i in range(0, 5):
    rowSum = 0
    for a in matrix[i]:
        rowSum += a
    rowSums.append(rowSum)

maxRowIndex = 0
for i in range(1, 5):
    if rowSums[i] > rowSums[maxRowIndex]:
        maxRowIndex = i

print(f"Index of row with max sum: {maxRowIndex}, sum: {rowSums[maxRowIndex]}")