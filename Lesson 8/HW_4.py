# Склад оргтехники


class Warehouse:
    __place = 60
    __equipment = []

    def __init__(self):
        self._name = str('Склад оргтехники')
        self._location = str('Место расположения: г. Рязань, Московское ш., д. 147')
        self._work_time = str('Время работы: Ежедневно с 8:00 до 20:00')

    def free_place(self):
        self.__place = Warehouse.__place - len(Warehouse.__equipment)
        return f'Свободных мест на складе: {self.__place}'


class OfficeEquipment(Warehouse):

    def __init__(self):
        self.title = str('Наименование: Оргтехника')
        self.description = str('Описание: Техническое оборудование офиса')
        self.model = {'Модельный ряд': ['HP', 'Xerox', 'Canon']}
        super().__init__()


class Printer(OfficeEquipment):

    def __init__(self):
        self.type = {'Тип': ['Струйный', 'Лазерный']}
        super().__init__()


class Scanner(OfficeEquipment):

    def __init__(self):
        self.function = {'Автоматическая подача докуметов': ['Есть', 'Нет']}
        super().__init__()


class Xerox(OfficeEquipment):

    def __init__(self):
        self.printing = {'Наличие цветной печати': ['Есть', 'Нет']}
        self.compatibility = {'Совместимость с компьютером': ['Есть', 'Нет']}
        super().__init__()


warehouse = Warehouse()
org = OfficeEquipment()
printer = Printer()
scanner = Scanner()
xerox = Xerox()
print(1)
