# Задача №37. Решение в группах

# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).

# Input: 2 -> 3 4
# Output: 4 3

def vvod(value):
    x = input('Введите число: ')
    if value == 1:
        return x
    return vvod(value - 1) + x

n = int(input('Введите количество: '))
print(vvod(n))
