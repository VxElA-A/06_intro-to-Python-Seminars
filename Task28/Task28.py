# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

def sum(x, y):
    if x or y == 1:
        return x + y
    return sum(x-1, y-1)

a = int(input('Введите число А: '))
b = int(input('Введите число Б: '))

print(sum(a, b))