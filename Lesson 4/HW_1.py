from sys import argv
script_name, production, rate, bonus = argv   # параметры скрипта
# Введите в командную строку следующую команду: HW_1.py 'Выработка в часах' 'Ставка в час' 'Премия'
# где параметры скрипта должны быть числовыми значениями, например: HW_1.py 40 200 300.5
print('Имя скрипта: ', script_name)
print('Выработка в часах: ', production)
print('Ставка в час: ', rate)
print('Премия: ', bonus)


def salary(production, rate, bonus):   # функция, вычисляющая заработную плату
    try:
        salary = float(production)*float(rate) + float(bonus)
    except ValueError:
        return print('Неверно введены параметры')
    return salary


print(f'Заработная плата составляет: {salary(production, rate, bonus)}')
