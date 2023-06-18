# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

# n = int(input("Введите количество элементов в массиве N: "))
# first = []
# for i in range(n):
#     first.append(input(f"Введите {i} элемент множества: "))
# print(f'Введенный массив: {first}')

first = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

max = int(input("Введите МАКСИМУМ диапазона: "))
min = int(input("Введите МИНИМУМ диапазона: "))

second = []
count = 0
for i in range(len(first)):
    if min <= first[i] <= max:
        second.append(i)
print(f'Получившийся массив индексов: {second}')
