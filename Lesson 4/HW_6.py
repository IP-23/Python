# Бесконечные итераторы
"""
from itertools import count
start = int(input('С какого числа начать генерирование? '))
finish = int(input('До какого числа осуществлять генерацию? '))
for el in count(start):
    if el > finish:
        break
    else:
        print(el)
"""

from itertools import cycle
finish = int(input('Введите количество итераций: '))
k = 1
for el in cycle([1, 2, 3]):
    if k > finish:
        break
    else:
        print(el)
        k += 1
