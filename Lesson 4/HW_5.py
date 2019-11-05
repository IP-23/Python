# Формироание списка четных элементов от 100 до 1000. Сумма элементов списка.

from functools import reduce
new_list = [el for el in range(99, 1001) if el % 2 == 0]
sum_all = reduce(lambda x, y: x * y, new_list)

print(f'Сумма элементов списка равна: {sum_all}')
