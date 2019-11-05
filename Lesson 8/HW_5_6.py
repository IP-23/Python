# Склад оргтехники. Прием и обработка товара на складе.


class Warehouse:
    __place = 60
    _equipment = ['Принтер', 'Сканер', 'Ксерокс']

    def __init__(self):
        self._name = str('Склад оргтехники')
        self._location = str('Место расположения: г. Рязань, Московское ш., д. 147')
        self._work_time = str('Время работы: Ежедневно с 8:00 до 20:00')

    def free_place(self):
        self.__place = Warehouse.__place
        return f'Свободных мест на складе: {self.__place}'

    @classmethod
    def data(cls, self):
        data_gd = {}
        for i in range(len(self._equipment)):
            try:
                data_rc = input(f'Сколько товаров {self._equipment[i]} приняли на склад? ')
                data_tr = input(f'Сколько товаров {self._equipment[i]}  отправили со склада? ')
                data_gd[self._equipment[i]] = int(data_rc) - int(data_tr)
            except ValueError:
                print('Данные введены неверно')
                break
        return f'На складе имеется: {data_gd}'

    @staticmethod
    def receive():
        goods_rc = input('Введите наименование товара для приема: ')
        number_rc = int(input('Введите количество:'))
        Warehouse.__place = Warehouse.__place - number_rc
        return f'Свободных мест на складе: {Warehouse.__place}'

    @staticmethod
    def transfer():
        goods_tr = input('Введите наименование товара для передачи: ')
        number_tr = int(input('Введите количество:'))
        department = input('Введите подразделение: ')
        Warehouse.__place = Warehouse.__place + number_tr
        return f'Товар {goods_tr} отправлен в : {department} в количестве {number_tr} шт.'


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
