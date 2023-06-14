# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.

# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# Моё решение:

n = int(input('Введите чсисло оценок: '))

spisok = list()
for i in range(n):
    x = int(input(f'Введите {i+1}-ю оценку: '))
    spisok.append(x)

print(' ')
print('Васины оценки: ')
print(*spisok)

spisok2 = list()
max = 0
min = 1
for i in range(len(spisok)):
    if spisok[i] < min:
        min = spisok[i]
    elif spisok[i] > max:
        max = spisok[i]
for i in range(len(spisok)):
    if spisok[i] == max:
        spisok[i] = min
        spisok2.append(spisok[i])
    else:
        spisok2.append(spisok[i])

print(' ')
print('Васины оценки без максимума: ')
print(*spisok2)


# То же решение только короче:

# ocenki = [int(x) for x in input('Введите оценки: ').split()]
# max0 = max(ocenki)
# for i in range(len(ocenki)):
#     if ocenki[i] == max0:
#         ocenki[i] = min(ocenki)
# print(*ocenki)
        
