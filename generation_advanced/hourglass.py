# Hourglass

# Task:
# Calculate the hourglass sum in A, then print the maximum hourglass sum

# Input Format

# There are 6 lines of input, where each line contains 6 space-sparated integers describing 2D Array A;
# every value in A will be in the inclusive range of -9 to 9.

# Constraints

# -9 <= A[i][j] <= 9
# 0 <= i, j <= 5

import sys

if __name__ == '__main__':

    arr = [ [1, 1, 1, 0, 0, 0],
            [0, 2, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 1, 1]]

def _get_hourglass_sum(matrix, row, col):
    sum = 0
    sum += matrix[row-1][col-1]
    sum += matrix[row-1][col]
    sum += matrix[row-1][col+1]
    sum += matrix[row][col]
    sum += matrix[row+1][col-1]
    sum += matrix[row+1][col]
    sum += matrix[row+1][col+1]
    return sum

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=' ')
    print()

max_hourglass_sum = -63

for i in range(1, 5):
    for j in range(1, 5):
        current_hourglass_sum = _get_hourglass_sum(arr, i, j)
        if current_hourglass_sum > max_hourglass_sum:
            max_hourglass_sum = current_hourglass_sum


print(max_hourglass_sum)