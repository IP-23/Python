# Создание класса "Дорога". Расчет массы асфальта.


class Road:
    _length = 0
    _width = 0

    def __init__(self, _length=0, _width=0):
        self._length = input('Введите длину дороги, м: ')
        self._width = input('Введите ширину дороги, м: ')

    def m_asphalt(self):
        mass_0 = input('Введите массу для покрытия одного кв.м дороги асфальтом, кг: ')
        thickness = input('Введите ширину толщину полотна, см: ')
        try:
            mass = float(self._length) * float(self._width) * float(mass_0) * float(thickness)
            print(f'Масса асфальта для покрытия всего дорожного полотна, кг =  {mass}')
        except ValueError:
            print('Вы ввели неверно данные')


road_ex = Road()
print(1)
