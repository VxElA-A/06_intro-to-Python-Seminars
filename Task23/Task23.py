# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)

# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# data = [int(i) for i in input("Введите числа: ").split()]

data = [0, -1, 5, 2, 3]
print(*list(data))
x = 0
for i in range(len(data) - 1):
    if data[i] < data[i + 1]:
        x += 1
print(x)

# data = [0, -1, 5, 2, 3]
# print(sum([int(data[i + 1] > data[i]) for i in range(len(data)-1)]))

# data = [0, -1, 5, 2, 3]
# for i in data:
#     print(i)


# data = [0, -1, 5, 2, 3]
# for i in range(len(data)):
#     print(data[i])

# data = [0, -1, 5, 2, 3]
# # x = 0
# for i in data:
#     if i < i + 1:
#         # x += 1
#         print(i)

# data = [0, -1, 5, 2, 3]
# print(*list(data))
# x = 0
# for i in range(len(data) - 1):
#     if data[i] < data[i + 1]:
#         x += 1
# print(x)