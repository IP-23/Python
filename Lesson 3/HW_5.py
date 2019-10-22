# Суммирование введенных элементов


def my_func(input_list):
    """Возвращает сумму введенных элементов"""
    list_new = input_list.split(' ')   # разделение строки на отдельные элементы
    my_sum = 0   # обнуление итоговой суммы
    try:
        for i in range(len(list_new)):   # цикл суммирования элементов
            if list_new[i] != 'стоп':
                my_sum += float(list_new[i])
                i += 1
            else:
                break
    except ValueError:
        return print('Вы неверно ввели числа')
    return my_sum


# Сделаем так, чтобы после завершения суммирования первой строки, сразу выводилась следующая
s = 0   # обнуляем сумму между элементами строк

while 1:
    input_list = str(input('Введите числа через пробел, например, 1 2.2 -3: '))   # ввод строки
    try:
        s += my_func(input_list)
        print(f'Сумма элементов равна: {s:.3f}')
        if 'стоп' in input_list:   # проверка на наличие спец. символа, завершающего суммирование
            break
    except TypeError or ValueError:
        continue

