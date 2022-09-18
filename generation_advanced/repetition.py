# 2.1

# Индекс массы тела

# m = float(input())
# h = float(input())
# index_mass = float(m / (h*h)) 

# if index_mass < 18.5:
#     print ("Недостаточная масса")
# elif index_mass > 25:
#     print ("Избыточная масса")
# else: print("Оптимальная масса")

# Стоимость строки

# l = input()
# rub = len(l) * 0.6
# kop = len(l) * 60 % 100
# print(int(rub), 'р.', kop, 'коп.')

# Количество слов

# a = str(input()).split()
# print(len(a))

# Зодиак

# z = ["Дракон", "Змея", "Лошадь", "Овца", "Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц"]
# year = int(input())
# print(z[year % 12-8])

# Переворот числа

# n = input()
# n1 = n[0:-5]
# n2 = n[:-6:-1]
# n3 = int(n1 + n2)
# print(n3)

# Standard American Convention

# num = int(input())
# print(f'{num:,}')

# Задача Иосифа Флавия

# n = 2
# k = 1

# surv = 0
# for i in range(1, n + 1):
#     surv = (surv + k) % i
# print(surv + 1)

# Координатные четверти

# number = int(input())
# first, second, third, fourth = 0, 0, 0, 0

# for _ in range(number):
#     x, y = map(int, input().split())
#     first += x > 0 and y > 0
#     second += x < 0 and y > 0
#     third += x < 0 and y < 0
#     fourth += x > 0 and y < 0

# print(f"Первая четверть: {first}")
# print(f"Вторая четверть: {second}")
# print(f"Третья четверть: {third}")
# print(f"Четвертая четверть: {fourth}")

# Больше предыдущего

# numbers = [int(n) for n in input().split()]
# counter = 0

# for i in range(1, len(numbers)):
#     if numbers[i] > numbers[i - 1]:
#         counter += 1
        
# print(counter)

# Назад, вперёд и наоборот

# На вход программе подается строка текста из натуральных чисел. Из неё формируется список чисел. 
# Напишите программу подсчета количества чисел, которые больше предшествующего им в этом списке числа, то есть, стоят вслед за меньшим числом. 

# nums = [int(i) for i in input().split()]
# for i in range(0, len(nums) - 1, 2):
#     nums[i], nums[i + 1] = nums[i + 1], nums[i]
# print(*nums)

# Сдвиг в развитии

# Sample Input 1:

# 1 2 3 4 5

# Sample Output 1:

# 5 1 2 3 4

# n = list(map(int, input().split()))
# n.insert(0, n[-1])
# del n[-1]
# print(*n)

# Произведение чисел

# Sample Input 1:

# 3
# 33
# 17
# 35
# 999

# Sample Output 1:

# НЕТ

# l = [int(input()) for n in range(int(input()))]
# n = int(input())

# fl = False 

# for i in range(len(l)):
#     for j in range(i + 1, len(l)):
#         if l[i] * l[j] == n:
#             fl = True
#             break
            
# print('ДА' if fl == True else 'НЕТ')

# Кремниевая долина

# Sample Input 1:

# 6
# 222anton456
# a1n1t1o1n1
# 0000a0000n00t00000o000000n
# gylfole
# richard
# ant0n

# Sample Output 1:

# 1 2 3

# virus = 'anton'

# for i in range(1, int(input()) + 1):
#     s, res = input(),  ''
#     for j in virus:
#         if j in s:
#             res += j
#             s = s[s.find(j):]
        
#     if res == 'anton':
#         print(i, end=' ')
#         continue


# Роскомнадзор запретил букву а 

# word = 'роскомнадзор' + ' запретил букву'
# alpha = [chr(i) for i in range(1072, 1104)]

# for letter in alpha:
#     if letter in word:
#         print(word, letter)
#         word = word.replace(letter, '').replace('  ', ' ').strip()

