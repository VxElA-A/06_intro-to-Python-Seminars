# Задача №57. Решение в группах
# 1. Прочесть с помощью pandas файл
# california_housing_test.csv, который находится в папке
# sample_data
# 2. Посмотреть сколько в нем строк и столбцов
# 3. Определить какой тип данных имеют столбцы

# Решение:

# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population):

# Вариант 1 (мой вариант):
# df[df['population'] < 500]['median_house_value'].mean()

# Вариант 2 (семинарский):
# a = df[df['population'] < 500]
# a['median_house_value'].mean()

# # print('-------------------------------------------------')

# Узнать какая максимальная households в зоне минимального значения population

# Вариант 1 (мой вариант):
# am = df['population'].min()
# df[df['population'] == am]['households'].max()

# Вариант 1 (мой вариант в одну строчку):
# df[df['population'] == df['population'].min()]['households'].max()

# Вариант 2 (семинарский):
# a = df[df['population'] == df['population'].min()]
# a['households'].max()