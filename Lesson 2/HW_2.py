# Обмен значений соседних элементов списка

# Введем строку, содержащую список элементов
list_input = str(input("Введите список через запятую (пример: 1, 2, 3): "))

# Разобьем строку на список элементов
list_new = list_input.split(', ')
print(list_new)   # вывод списка на экран

length = len(list_new)   # определение длины списка
i = 0   # обнуление счетчика индекса элементов

while i + 1 < length:   # цикл по перестановке соседних элементов списка
    list_new[i], list_new[i+1] = list_new[i+1], list_new[i]   # осуществление перестановки соседних элементов
    i += 2

print(list_new)   # вывод итогового списка








