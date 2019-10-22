# Факториал чисел до 15 включительно
from functools import reduce


def fibo_gen():     # функция вычисляющая факториал
    factorial = 1   # начальное значение факториала
    while True:
        if factorial < 1:
            factorial = 1   # факториал единицы
        else:
            # вычисление факториалов от 1 до 15
            yield reduce(lambda x, y: x * y, range(1, factorial+1))
        print()
        factorial += 1


# Генератор списка с порядковым номером и значением факториала
for i, fact in enumerate(fibo_gen(), 1):
    if i <= 15:
        print(i, fact)
    else:
        break
