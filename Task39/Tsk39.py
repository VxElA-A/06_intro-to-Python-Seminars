# Даны два массива чисел. Требуется вывести те элементы первого массива 
# (в том порядке, в каком они идут в первом массиве),
# которых нет во втором массиве. Пользователь вводит  число N - количество элементов в первом массиве,
# затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве.
# Затем элементы второго массива.

# Ввод: 					Вывод:
# 7					    3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1

# Решение 1
# n = int(input())
# list_1 = [int(i) for i in input().split()][:n]
# m = int(input())
# list_2 = [int(i) for i in input().split()][:m]
# for elem in list_1:
#     if elem not in list_2:
#         print(elem, end=' ')

# # Решение 2
# n = int(input())
# list_1 = [int(i) for i in input().split()][:n]
# m = int(input())
# list_2 = [int(i) for i in input().split()][:m]
# print([x for x in list_1 if x not in list_2])

# Решение №3, здесь "n" и "m" никак не увзанны с массивами, хотя должны ограничивать "собой" число элементов. В решении 1 и 2 это ограничение есть.
# n = int(input('Введите число: '))
# list1 = [int(i) for i in input('Введите массив через пробел: ').split()]
# m = int(input('Введите число: '))
# list2 = [int(i) for i in input('Введите массив через пробел: ').split()]
# for i in list1:
#     if i not in list2:
#         print(i, end=" ")

# Решение 4 - ввод кол-ва элементов и самого массива здесь реализован прикольнее с точки зрения пользовательского взаимодействия, однако вторая часть где вывод, мне как новичку менее понятна.
# n = int(input('Введите n: '))
# lst_one = [int(input(f'Введите {i + 1}-е число первого массива: ')) for i in range(n)]
# m = int(input('Введите m: '))
# lst_two = [int(input(f'Введите {i + 1}-е число: второго массива')) for i in range(m)]

# print(*[num for num in lst_one if num not in lst_two])
