# Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном массиве выведет количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного.
# Сначала вводится число N — количество элементов в массиве  Далее записаны N чисел — элементы массива.
# Массив состоит из целых чисел.

# Ввод: 		Ввод:
# 5				5
# 1 2 3 4 5		1 5 1 5 1

# Вывод:		Вывод:
# 0				2

# n = int(input('Введите число элементов массива: '))
# list_1 = [int(i) for i in input(
#     'Введите массив - целые числа через пробел: ').split()][:n]
# count = 0
# for i in range(len(list_1) - 1):
#     if list_1[i-1] < list_1[i] > list_1[i+1]:
#         count = count + 1
# print(count)

# Решение (с оптимизацией)
# n = int(input())
# list_1 = [int(i) for i in input().split()][:n]
# print(sum([int(list_1[i - 1] < list_1[i] > list_1[i + 1]) for i in range(1, n - 1)]))

n = int(input("Введите количество элементов в массиве N: "))
first = []
for i in range(n):
    first.append(input(f"Введите {i} элемент множества: "))
print(f'Введенный массив: {first}')

count = 0
for i in range(len(first)-1):
    if first[i] < first[i+1] > first[i+2]:
        count = count + 1
print(count)
