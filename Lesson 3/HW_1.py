# Деление чисел


def my_div():
    """Возвращает частное от деления"""
    var_1 = float(input('Введите делимое: '))
    var_2 = float(input('Введите делитель: '))
    if var_2 != 0:      # если делитель не равен нулю, то осуществляем деление
        div = var_1 / var_2
    else:
        div = str('Делить на ноль нельзя!')
    return div


print('Частное: ', my_div())

