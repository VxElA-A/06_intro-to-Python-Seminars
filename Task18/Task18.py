# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X

# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input('Введите количество элементов в массиве: '))
i = 1
result = set()
while i <= n:
    result.add(i)
    i += 1
print(*result)
x = int(input('Введите число поиска: '))
value = 0
for i in result:
    if i <= x:
        value = i
print(f'-> {value}')
