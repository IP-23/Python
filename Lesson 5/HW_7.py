# Финансовые результаты фирм
import re
import json

firm_profit = {}   # создание словаря с прибыльными фирмами
firm_cost = {}     # создание словаря с убыточными фирмами
with open('HW_7.txt', 'r+', encoding="utf-8") as file:
    for line in file:
        outcome = re.findall(r"\d+", line)  # поиск всех чисел в строке и занесение их в список
        firm = re.findall(r'\w+', line)     # поиск слов и чисел в строке с занесением в новый список
        profit = int(outcome[-2]) - int(outcome[-1])  # вычисление фин.результата фирмы
        if profit >= 0:
            firm_profit[firm[0]] = profit
        else:
            firm_cost[firm[0]] = profit
    average_pr_dict = {'average_profit': sum(firm_profit.values()) / len(firm_profit)}     # вычисление ср. прибыли
    list_firm = [firm_profit, average_pr_dict]   # создание списка, где первый элемент - словарь с прибыльными фирмали
    json.dump(list_firm, file)   # запись списка в исходный файл

print(f'Фирмы, имеющие неотрицательную прибыль: {list_firm}')
print(f'Фирмы, имеющие убытки: {firm_cost}')

