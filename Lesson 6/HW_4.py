# Создание классов с различными типами машин
import random


class Car:
    def __init__(self):
        self.speed = random.randrange(0, 60)
        self.color = random.choice(('Grey', 'White', 'Black', 'White and Blue', 'Red'))
        self.name = random.choice(('Mazda', 'LADA', 'Kia', 'BMW', 'Hyundai', 'Ford'))

    def go(self):
        if self.speed > 0:
            print('Машина едет')

    def stop(self):
        if self.speed == 0:
            print('Машина остановилась')
        else:
            print('Машина едет, скорость равна, км/ч: ', self.speed)

    def direction(self):
        if self.speed > 0:
            direction = random.choice(('Машина едет прямо', 'Машина повернула налево', 'Машина повернула направо'))
            print(direction)


class TownCar(Car):
    def __init__(self):
        self.is_police = 'Нет'
        super().__init__()


class SportCar(Car):
    def __init__(self):
        self.is_police = 'Нет'
        super().__init__()


class WorkCar(Car):
    def __init__(self):
        self.is_police = 'Нет'
        super().__init__()


class PoliceCar(Car):
    def __init__(self):
        self.is_police = 'Да'
        super().__init__()


car_tw = TownCar()
car_sp = SportCar()
car_w = WorkCar()
car_police = PoliceCar()
print(1)
