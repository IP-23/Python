# Формирование словаря об учебном предмете

import re
dict_new = {}   # создание пустого словаря
with open('HW_6.txt', encoding="utf-8") as file:
    for line in file:
        hours = re.findall(r"\d+", line)   # поиск всех чисел в строке и занесение их в список
        subjects_list = re.findall(r'\w+', line)   # поиск слов и чисел в строке с занесением в новый список
        sum_hours = 0   # обнуление сумматора количества занятий (часов)
        for i in range(len(hours)):
            sum_hours = sum_hours + int(hours[i])
        # Создание словаря, где ключами явл. нулевые эл-ты списка subjects_list, а значениями - суммарное кол-во занятий
        dict_new[subjects_list[0]] = sum_hours
print(dict_new)

