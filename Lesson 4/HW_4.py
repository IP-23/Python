# Неповторяющиеся элементы списка
input_list = str(input('Введите список элементов через запятую (пример: 1, 2, 3): '))
input_list = input_list.split(', ')

list_new = [el for el in input_list if input_list.count(el) == 1]

print(f'Новый список: {list_new}')
