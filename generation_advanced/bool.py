num1 = 3 * True - (True + False)
num2 = (True + True + False) ** 3 + 5
print(num1 + num2)

numbers = [-6, -8, 0, 1, 3, 8, -7, 12, 17, 24, 25, 3, 5, 1]
res = 0
for num in numbers:
    res += (num % 2 == 1) and (num > 1) 
print(res)