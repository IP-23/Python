# Создание классов с канцелярскими товарами


class Stationery:
    title = None

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self):
        title = 'Ручка'
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки ручки')


class Pencil(Stationery):
    def __init__(self):
        title = 'Карандаш'
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки карандаша')


class Handle(Stationery):
    def __init__(self):
        title = 'Маркер'
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки маркера')


stationery = Stationery('Канцелярские товары')
pen = Pen()
pencil = Pencil()
handle = Handle()
print(1)
