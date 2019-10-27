# Вывод полного имени работника и его заработной платы


class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {'profit': [20000, 30000, 40000], 'bonus': [5000, 8000, 12000]}


class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        print(f'{self.name} {self.surname} - {self.position}')

    def get_full_profit(self):
        slr = list(self.__income.values())   # преобразование словаря в список, содержащий: 1-ый список - оклады, 2-ой список - премии
        i = 0   # обнуление счетчика для определения зп работников по категориям
        if self.position == 'экономист':
            salary = slr[0][i] + slr[1][i]   # 20000 + 5000
            print(f'{self.name} {self.surname} получает: {salary} т.р')
        elif self.position == 'экономист-аналитик':
            i += 1
            salary = slr[0][i] + slr[1][i]   # 30000 + 8000
            print(f'{self.name} {self.surname} получает: {salary} т.р')
        elif self.position == 'руководитель':
            i += 2
            salary = slr[0][i] + slr[1][i]   # 40000 + 12000
            print(f'{self.name} {self.surname} получает: {salary} т.р')


worker_0 = Position('Иван', 'Иванов', 'руководитель')
worker_1 = Position('Алексей', 'Алексеев', 'экономист-аналитик')
worker_2 = Position('Семён', 'Семёнов', 'экономист')
print(1)
