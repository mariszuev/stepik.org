# words = ['Hello', 'Python']
# print('-'.join(words))

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)

# print(list1)

# list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
# sub_list = ['h', 'i', 'j']

# list1[2][1][2].extend(sub_list)

# print(list1)

# list1 = [[1, 8, 7, 4], [1, 3, 4, 5, 6], [2, 7, 2], [2, 6, 7, 8]]
# print(max(list1))

# list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = -1

# for i in list1:
#     if max(i) > maximum:
#         maximum = max(i)

# print(maximum)


# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]

# for i in list1:
#     i.reverse()

# print(list1)

# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# total = 0
# counter = 0

# for i in list1:
#     for j in i:
#         total += j
#         counter += 1
# print(total / counter)

# list1 = [[1] * 3] * 3
# list1[0][1] = 5

# my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]

# maximum = my_list[0][0]
# minimum = my_list[0][0]

# print(maximum, minimum)

# for row in my_list:
#     print(row)
#     maximum = max(row)
#     minimum = min(row)

# print(maximum, minimum)

# n = 5
# list = [[j for j in range(1, n + 1)] for i in range(1, n + 1)]
# print(*list, sep='\n')

# n = 3
# list = [[j for j in range(1, i + 1)] for i in range(1, n + 1)]
# print(*list, sep='\n')

# Pascal's Triangle

# n = 5
# list1 = []

# for i in range(n):
#     temp_list = []
#     for j in range(i + 1):
#         if j == 0 or j == i:
#             temp_list.append(1) 
#         else:
#             temp_list.append(list1[i - 1][j - 1] + list1[i - 1][j])
#     list1.append(temp_list)

# for i in range(n):
#     for j in range(n - i - 1):
#         print(" ", end="")
#     for j in range(i + 1):
#         print(list1[i][j], end=" ")
#     print()

# n = int(input())
# s = []
# for i in range(n+1):
#     row=[1]*(i+1)
#     for j in range(i+1):
#         if j!=i and j!=0: row[j] = s[i-1][j-1]+s[i-1][j]
#     s.append(row)
# print(s[n] if n!=0 else [1])

# text_sample = []
# for i in input().split():
#     if text_sample and i in text_sample[-1]:
#         text_sample[-1].append(i)
#     else:
#         text_sample.append([i])
# print(text_sample)
