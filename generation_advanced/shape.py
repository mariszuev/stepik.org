n = 5

# Square

# for i in range(n):
#     for j in range(n):
#         print('*', end=' ')
#     print()

# for i in range(n):
#     print('* ' * n)

# Triangle

# for i in range(1, n + 1):
#     print(' ' * (n - i) + '* ' * i)

# Right triangle

# for i in range(1, n + 1):
#     print('* ' * i)

# Left triangle

# for i in range(1, n + 1):
#     print('  ' * (n - i) + '* ' * i)

# Diamond

# for i in range(1, n + 1):
#     print(' ' * (n - i) + '* ' * i)
# for i in range(n - 1, 0, -1):
#     print(' ' * (n - i) + '* ' * i)

# Triangle reverse

# for i in range(n, 0, -1):
#     print(' ' * (n - i) + '* ' * i)

# Right triangle reverse

# for i in range(n, 0, -1):
#     print('* ' * i)

# Left triangle reverse

# for i in range(n, 0, -1):
#     print('  ' * (n - i) + '* ' * i)

# Arrow right

# for i in range(1, n + 1):
#     print('* ' * i)
# for i in range(n - 1, 0, -1):
#     print('* ' * i)

# Arrow left

for i in range(1, n + 1):
    print('  ' * (n - i) + '* ' * i)
for i in range(n, 0, -1):
    print('  ' * (n - i) + '* ' * i)