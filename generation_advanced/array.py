# rows, cols = 3, 4  # rows - количество строк, cols - количество столбцов

# matrix  = [[2, 3, 1, 0],
#            [9, 4, 6, 8],
#            [4, 7, 2, 7]]

# for r in range(rows):
#     for c in range(cols):
#         print(matrix[r][c], end=' ')
#     print()

# print()

# for c in range(cols):
#     for r in range(rows):
#         print(matrix[r][c], end=' ')
#     print()


# 4.3 - ex. 13

# st = "a b c d e f"
# n = 2

# st = st.split()
# a = [[] for _ in range(0, len(st), n)]
# for i in range(len(a)):
#     a[i].extend(st[:n])
#     st = st[n:]
# print(a)

# 4.3 - ex. 14

# n = "a b c"

# n = n.split()

# a = [[]]
# k = 1
# while k != len(n) + 1:
#   for j in range(len(n)):
#     print(n[j:j + k])
#     print(j)
#     print(k)
#     if len(n[j:j + k]) == k:
#       a.append(n[j:j+k])
#   k += 1
# print(a)

# 4.4 - ex. 6

# n = 4 # row
# m = 2 # column

# rows, cols = (n, m)
# arr=[]

# for i in range(rows):
#     col = []
#     for j in range(cols):
#         col.append(input())
#     arr.append(col)
# print(*[' '.join(x) for x in arr], sep="\n")

# print()

# for c in range(m):
#     for r in range(n):
#         print(arr[r][c], end=' ')
#     print()

# st = [  ['и', 'швец'],
#         ['и', 'жнец'],
#         ['и', 'на'],
#         ['дуде', 'игрец']
#     ]

# for item in (st):
#     print(' '.join(item))

# print()

# for c in range(m):
#     for r in range(n):
#         print(st[r][c], end=' ')
#     print()

# rows, cols = (3, 3)
# arr=[]
# for i in range(rows):
#     col = []
#     for j in range(cols):
#         col.append((input().split())
#     arr.append(col)
# print(arr)

# arr1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# count = 0
# for r in range(rows):
#     for c in range(cols):
#         if c == r:
#             count += arr1[r][c]
# print(count)


# x = '1 2 3'
# arr2 = []
# x = x.split()
# print(x)

# 4.4 - ex. 9

# x = int(input())
# a = []
# for i in range(x):
#     a.append(input().split())
    
# count = 0
# for r in range(x):
#     for c in range(x):
#         if c == r:
#             count += int(a[r][c])
# print(count)

# matrix  = [[1, 2, 3, 4],
#            [5, 6, 3, 15],
#            [0, 2, 3, 1],
#            [5, 2, 8, 5]]

# rows, cols = (4, 4)

# counter = 0

# for i in matrix:
#     sr = (sum(list(map(int, i)))) / len(i)
#     for j in i:
#         if int(j) > sr:
#             counter += 1
#     print(counter)
#     counter = 0

# n = 4
# l = [input().split() for _ in range(n)]
# l = [[1, 4, 5],
#      [6, 7, 8],
#      [1, 1, 6]]

# l = [[6, 0],
#      [7, 9]]

# l = [[1, 9, 5, 8],
#     [6, 7, 8, 6],
#     [1, 1, 6, 2],
#     [2, 7, 4, 6]]


# l = [[1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [3, 4, 5, 6],
#     [1, 2, 3, 4]]


# rows, cols = (n, n)
# a = []
# for r in range(n):
#     for c in range(n):
#         if r >= c:
#             a.append(l[r][c])
# print(max(a))

# h4 = 0
# r4 = 0
# d4 = 0
# l4 = 0

# for r in range(n):
#     for c in range(n):
#         if r > c and r < n - 1 - c:
#             l4 += l[r][c]
#         elif r < c and r < n - 1 - c:
#             h4 += l[r][c]
#         elif r < c and r > n - 1 - c:
#             r4 += l[r][c]
#         elif r > c and r > n - 1 - c:
#             d4 += l[r][c]

# print(f'Верхняя четверть: {h4}')
# print(f'Правая четверть: {r4}')
# print(f'Нижняя четверть: {d4}')
# print(f'Левая четверть: {l4}')


# rows, cols = 3, 4         

# matrix  = [[277, -930, 11, 0],
#            [9, 43, 6, 87],
#            [4456, 8, 290, 7]]

# for r in range(rows):
#     for c in range(cols):
#         print(str(matrix[r][c]).ljust(6), end='')
#     print()

# 4.5 - ex. 1

# Таблица умножения

# n = 4
# m = 6

# mult = []

# for r in range(n):
#     col = []
#     for c in range(m):
#         col.append(r * c)
#     mult.append(col)

# for r in range(n):
#     for c in range(m):
#         print(str(mult[r][c]).ljust(3), end='')
#     print()

# 4.5 - ex. 2

# Максимум в таблице

# n = 6
# m = 8

# matrix = [[-4, -3, -4, -4, -1, -8, -2, -3],
#     [-2, -3, -9, -7, -3, -4, -4, -5],
#     [-4, -3, -4, -4, -1, -2, -2, -3],
#     [-2, -3, -9, -3, -3, -1, -4, -5],
#     [-5, -3, -4, -4, -1, -2, -2, -3],
#     [-2, -3, -7, -8, -3, -4, -4, -5]]
    
# # n, m = int(input()), int(input())
# # matrix = [[int(i) for i in input().split()] for _ in range(n)]
# row, col = (0, 0)

# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] > matrix[row][col]:
#             row,col = i, j
            
# print(row, col)

# 4.5 - ex. 3

# Обмен столбцов

# matrix = [[11, 12, 13, 14],
#           [21, 22, 23, 24],
#           [31, 32, 33, 34]]

# n, m = (3, 4)
# i, j = (0, 1)

# for row in range(n):
#     for col in range(m): # 0
#         if col == i:
#             matrix[row][i], matrix[row][j] = matrix[row][j], matrix[row][i]
#         print(matrix[row][col], end=' ')
#     print()

# 4.5 - ex. 4

# Симметричная матрица

# n = 3

# matrix = [[0, 1, 2],
#           [1, 2, 7],
#           [2, 3, 4]]

# flag = 'YES'

# for r in range(n):
#     for c in range(n):
#         if r != c:
#             if matrix[r][c] != matrix[c][r]:
#                 flag = 'NO'
#                 break
# print(flag)

# 4.5 - ex. 5

# Обмен диагоналей

# matr = [[1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]]

# mult = []

# n = 3

# n = int(input())
# matr = [[int(i) for i in input().split()] for _ in range(n)]

# for i in range(n):
#     for j in range(n):
#         if (i == j) or (i == n - 1 - j):
#             print(matr[n - 1 - i][j], end=' ')
#         else:
#             print(matr[i][j], end=' ')
#     print()

# 4.5 - ex. 6

# Зеркальное отображение

# matr = [[1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]]

# n = 3

# n = int(input())
# matrix = [input().split() for _ in range(n)]

# for i in range(n // 2):
#     matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]
# for row in matrix:
#     print(*row)

# 4.5 - ex. 7

# Поворот матрицы

# matr = [[1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]]

# n = 3

# n = int(input())
# matrix = []

# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)

# for j in range(n):
#     for i in range(n - 1, -1, -1):
#         print(matr[i][j], end=' ')
#     print()

# 4.5 - ex. 8

# Ходы коня

# col, row = 'b', '6'

# arr = [['.']*col]*row

# for i in range(row):
#     for j in range(col):
#         print(arr[i][j], end=' ')
#     print()
 
# b6

# arr_col = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
# arr_row = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}


# arr = [["N" if [i, j] == [arr_row[row], arr_col[col]] else '.' for j in range(8)] for i in range(8)]

# for i in range(8):
#     for j in range(8):
#         if (arr_row[row] - i) * (arr_col[col] - j) in [-2, 2]:
#             arr[i][j] = "*"
# for line in arr:
#     print(*line, sep = ' ')

# 4.5 - ex. 9

# Магический квадрат

# matrix = [[8, 1, 6],
#         [3, 5, 7],
#         [4, 9, 2]]

# n = 3

# arr = sum(matrix[0])

# flag = 'YES'

# numbers = [i for i in range(1, n ** 2 + 1)]

# for i in range(n):
#     for j in range(n):
#         if matrix[i][j] in numbers:
#             numbers.remove(matrix[i][j])
#     if i == n - 1 and j == n - 1 and numbers != []:
#         flag = 'NO'

# for i in range(n):
#     if sum(matrix[i]) != arr:
#         flag = 'NO'
#         break

# for j in range(n):
#     result = 0
#     for i in range(n):
#         result += matrix[i][j]
#         if i == n - 1 and result != arr:
#             flag = 'NO'
#             break

# print(flag)

# 4.6 - ex. 1

# Шахматная доска

# x, y = (3, 4)

# matrix = [['.'] * y for _ in range(x)]

# for i in range(x):
#     for j in range(y):
#         if (i + j) % 2 != 0:
#             matrix[i][j] = '*'
#         print(matrix[i][j], end=' ')
#     print()