# Создание светофора
import time


class TrafficLight:
    __colour = ['красный', 'желтый', 'зелёный']

    def __init__(self):
        __colour = ['красный', 'желтый', 'зелёный']

    def running(self):
        self.__colour = TrafficLight.__colour
        while True:
            print(f'Цвет светофора: {self.__colour[0]}')
            time.sleep(7)   # задержка на 7 секуд
            print(f'Цвет светофора: {self.__colour[1]}')
            time.sleep(2)
            print(f'Цвет светофора: {self.__colour[2]}')
            time.sleep(7)


traffic_light = TrafficLight()
print(1)
