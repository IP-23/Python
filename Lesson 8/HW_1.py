# Проверка правильности введенной даты
import re


class Date:
    string = input('Введите дату в формате дд-мм-гг: ')
    data = ['День', 'Месяц', 'Год']
    list_string = re.findall(r"\d+", string)    # поиск чисел в строке и занесение их в новый список
    list_30 = [4, 6, 9, 11]     # список месяцев с количество дней равным 30
    list_31 = [1, 3, 5, 7, 8, 10, 12]   # список месяцев с количество дней равным 31
    @classmethod
    def my_func(cls):
        for i in range(len(Date.list_string)):
            Date.list_string[i] = int(Date.list_string[i])      # преобразование типа данных в типу "Число"
            print(f'Тип данных {Date.data[i]}: {type(Date.list_string[i])}')   # вывод типа данных

    @staticmethod
    def my_func_new():
        try:        # проверка логичности введенной даты
            if Date.list_string[1] < 13 and Date.list_string[2] > 0:
                if Date.list_string[1] == 2 and Date.list_string[0] <= 28:
                    print('Данные введены верно')
                elif Date.list_string[1] in Date.list_30 and Date.list_string[0] <= 30:
                    print('Данные введены верно')
                elif Date.list_string[1] in Date.list_31 and Date.list_string[0] <= 31:
                    print('Данные введены верно')
                else:
                    print('Не верно введен формат даты')
        except IndexError:
            print('Не верно введен формат даты. Проверьте данные')


if __name__ == '__main__':
    date = Date()
    date.my_func()
    Date.my_func_new()

