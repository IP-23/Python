# Определение сотрудников с окладом меньше 20000 тыс. Подсчет средней з/п сотрудников.

with open("HW_3.txt", encoding="utf-8") as file_new:
    salary = 0
    count_str = 0
    for line in file_new:   # для каждой строки в файле
        count_str += 1
        # Создание из строки списка, где первый элемент фамилия сотрудника, последний - з\п.
        line_list = line.split(' ')
        if int(line_list[-1]) < 20000:
            print(f'{line_list[0]} имеет оклад меньше 20000 тыс.: {line_list[-1]}')
        salary = salary + int(line_list[2])   # подсчет суммарной з\п.

print(f'Средняя величина доходов сотрудников: {salary/count_str} тыс.')
