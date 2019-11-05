# Создание собственного класса, обрабатывающего деление на ноль
class OwnZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))

try:
    if b == 0:
        raise OwnZeroDivisionError('На ноль делить нельзя.')    # вызов собственной ошибки
    else:
        print(a/b)
except OwnZeroDivisionError as e:
    print(e)

