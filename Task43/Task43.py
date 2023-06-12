# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.

# Ввод:			Вывод:
# 1 2 3 2 3			2

# list_1 = [int(i) for i in input().split()]
# result = {}
# for i in list_1:
#     if i in result:
#         result[i] += 1
#     else:
#         result[i] = 1
# print(sum([element // 2 for element in result.values()]))

n = int(input("Введите количество элементов списка: "))
list = []
for i in range(n):
    list.append(input(f"Введите {i+1}-й элемент списка: "))
print(f'Введенный массив: {list}')

count = 0
for i in range(len(list)-1):
        print(i)
        print('верхний цикл закончился')
        for j in range(i + 1, len(list)):
              print(j)
              print('нижний цикл закончился')
              if list[i] == list[j]:
                print(list[i], list[j])
                print('условие выполнилось')
                count = count + 1
print(count)


# n = int(input('Введите n: '))
# lst = [int(input(f'Введите {i + 1}-е число массива: ')) for i in range(n)]

# # print(sum([1 for i in range(len(lst)) for j in range(i + 1, len(lst)) if lst[i] == lst[j]]))
# count = 0
# for i in range(len(lst) - 1):
#     for j in range(i + 1, len(lst)):
#         if lst[i] == lst[j]:
#             count += 1
# print(count)