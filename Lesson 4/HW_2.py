# Вывод элементов исходного списка, значения которых больше предыдующего элемента
input_list = str(input('Введите список элементов через запятую: '))
input_list = input_list.split(', ')
new_list = []
i = 1
for i in range(len(input_list)):
    if input_list[i] > input_list[i-1]:
        new_list.append(input_list[i])
        i += 1
print(f'Новый список: {new_list}')
