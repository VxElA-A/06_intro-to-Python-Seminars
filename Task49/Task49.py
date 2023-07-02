# Задача №49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам. 
# Назовем самой далекой планетой ту, орбита которой имеет 
# самую большую площадь. Напишите функцию 
# find_farthest_orbit(list_of_orbits), которая среди списка орбит 
# планет найдет ту, по которой вращается самая далекая 
# планета. Круговые орбиты не учитывайте: вы знаете, что у 
# вашей звезды таких планет нет, зато искусственные спутники 
# были были запущены на круговые орбиты. Результатом 
# функции должен быть кортеж, содержащий длины полуосей 
# эллипса орбиты самой далекой планеты. Каждая орбита 
# представляет из себя кортеж из пары чисел - полуосей ее 
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, 
# где a и b - длины полуосей эллипса. При решении задачи 
# используйте списочные выражения. Подсказка: проще всего 
# будет найти эллипс в два шага: сначала вычислить самую 
# большую площадь эллипса, а затем найти и сам эллипс, 
# имеющий такую площадь. Гарантируется, что самая далекая 
# планета ровно одна
# Пример ввода и вывода данных представлены на
# следующем слайде

# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# def find_farthest_orbit (orbits):
#     orbits_change = [i for i in orbits if i[0] != i[1]]
#     areas_orbits = [i[0] * i[1] for i in orbits_change]
#     max_area_index = areas_orbits.index(max(areas_orbits))
#     # max_area_index = [i for i in areas_orbits if i == max(areas_orbits)][0]
#     return orbits_change[max_area_index]

# print(*find_farthest_orbit(orbits))

# Второй вариант:

# def find_farthest_orbit (orbits):
#     orbits_change = list(map(lambda x: x[0] * x[1] if x[0] != x[1] else 0, orbits))
#     return orbits[orbits_change.index(max(orbits_change))]

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

# РЕШАЮ САМ !!!!!.........////////////////////// Подсмотрел, но разобрался)

def find_farthest_orbit(list_of_orbits):
    orbits_change = list(map(lambda x: x[0] * x[1] if x[0] != x[1] else 0, list_of_orbits))
    print(orbits_change)
    return list_of_orbits[orbits_change.index(max(orbits_change))]
    
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))