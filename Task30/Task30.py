# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a

# n = a1 + (n-1) * d.

# Каждое число вводится с новой строки.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

n = int(input("Введите ПЕРВЫЙ элемент арифметической прогрессии: "))
d = int(input("Введите РАЗНОСТЬ арифметической прогрессии: "))
x = int(input("Введите КОЛИЧЕСТВО элементов в массиве прогрессии: "))
massiv = []
count = 1
for i in range(x):
    while count < n - 1:
        massiv.append(n + (count - 1) * d)
        count+=1
print(f'Введенный массив: {massiv}')


# a1 = int(input())
# d = int(input())
# n = int(input())
# for i in range(n):
#     print(a1 + i * d)