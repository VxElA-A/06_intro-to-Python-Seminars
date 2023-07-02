# import random
# import pandas as pd
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# print(data.head()) # Добавил принт к Заданию - обернул data.head() в print(внес сюда).

# Вариант решения №1 - длинная реализация, много строк - 20

# import random
# import pandas as pd
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# print(lst)
# print()
# data = pd.DataFrame({'whoAmI':lst})
# data.loc[data['whoAmI'] == 'robot', 'robot_group'] = '1'
# data.loc[data['whoAmI'] != 'robot', 'robot_group'] = '0'
# data.loc[data['whoAmI'] == 'human', 'human_group'] = '1'
# data.loc[data['whoAmI'] != 'human', 'human_group'] = '0'
# print(data.head(n=20))

# Вариант решения №2 - компактный вид и вывод в 5 строк как в задании.

import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

unique_values = data['whoAmI'].unique()
one_hot_data = pd.DataFrame()

for value in unique_values:
    one_hot_data[value] = (data['whoAmI'] == value).astype(int)

print(one_hot_data.head()) # Добавил принт к строке - one_hot_data.head() в print(внес сюда).