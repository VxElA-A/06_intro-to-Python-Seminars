# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по 
# счету числом Фибоначчи оно является, то есть 
# выведите такое число n, что φ(n)=A. Если А не 
# является числом Фибоначчи, выведите число -1.

# Input: 5
# Output: 6

# 0 1 1 2 3 5 8 13

n = int(input("Введите число: "))
a0 = 0
a1 = 1
result = 0
i = 2
while a1 < n:
    result = a0 + a1
    a0 = a1
    a1 = result
    i = i + 1
    if result > n:
        i = -1
if i == -1:
    print(i)
else:
    print(f'Ваше число по счету {i}-ое')
    