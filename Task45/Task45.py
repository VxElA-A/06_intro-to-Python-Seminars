# Два различных натуральных числа n и m называются дружественными,
# если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот.
# Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.
# Программа получает на вход одно натуральное число k, не превосходящее 105.
# Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k.
# Пары необходимо выводить по одной в строке, разделяя пробелами.
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).

# Ввод:		Вывод:
# 300			220 284

n = int(input())
list_1 = list()
for i in range(n):
    summa = 0
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            summa += j
    list_1.append((i, summa))
# print(list_1)

for i in range(len(list_1)):
    for j in range(i, len(list_1)): # можно вмето i поставить i+1 тогда необходимо убрать "i != j and" из следующей строки
        if i != j and list_1[i][0] == list_1[j][1] and list_1[i][1] == list_1[j][0]:
            print(*list_1[i])

# https://www.notion.so/Python-6fb8d8776a264dddbaff243f54d362ae?pvs=4

# самоучитель Питон:
# https://forproger.ru/tutorial/samouchitel-python


# def summ_of_dividers(number: int) -> int:
#     result = 0
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             result += i
#             k = number // i
#             if k != i:
#                 result += k
#     return result + 1

# k = int(input("Введите число: "))
# for i in range(k):
#     for j in range(i+1, k):
#         if summ_of_dividers(i) == j and summ_of_dividers(j) == i:
#             print(f"{i} {j}")
            