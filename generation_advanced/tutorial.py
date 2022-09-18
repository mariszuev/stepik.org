# Initialize a new 2D array [[1, 2, 3][4, 5, 6]].

# x = 0
# n, m = (2, 3)

# matrix = []
  
# for i in range(n):
#     row = []
#     for j in range(m):
#         row.append(x + 1)
#         x += 1
#     matrix.append(row)

# for i in range(n):
#     for j in range(m):
#         print(matrix[i][j], end=' ')
#     print()

# Function that adds up diagonal elements and returns the sum. 

# def diagonal_sum(z):
#     total = 0
#     for i in range(len(z)):
#         total += z[i][i]
#     return total
    
# x = 0
# n, m = (3, 3)

# matrix = []
  
# for i in range(n):
#     row = []
#     for j in range(m):
#         row.append(x + 1)
#         x += 1
#     matrix.append(row)

# for i in range(n):
#     for j in range(m):
#         print(matrix[i][j], end=' ')
#     print()

# print(diagonal_sum(matrix))

# Rooks

# def rooks_are_safe(chessboard):
#     x = len(chessboard)
#     for row_i in range(x):
#         row_count = 0
#         for col_i in range(x):
#             row_count += chessboard[row_i][col_i]
#         if row_count > 1:
#             return False
#     for col_i in range(x):
#         col_count = 0
#         for row_i in range(x):
#             col_count += chessboard[row_i][col_i]
#         if col_count > 1:
#             return False
#     return True

# n, m = (8, 8)

# chessboard = [[0 for i in range(m)] for j in range(n)]

# chessboard[1][1] = 1
# chessboard[0][1] = 1
# chessboard[4][-1] = 1

# # for i in range(n):
# #     for j in range(m):
# #         print(chessboard[i][j], end=' ')
# #     print()

# print(rooks_are_safe(chessboard))