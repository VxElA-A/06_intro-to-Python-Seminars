# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числавида 2k), не превосходящие числа N.

# 10 -> 1 2 4 8

n = int(input("Введите целое число: "))
i = 0
res = ''
s = ''
while 2**i <= n:
    s = f'{2**i}'
    res = res + s + ' '
    i += 1
print(res)