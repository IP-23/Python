# Проверка на наличие в списке булевых элементов и строк
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


number = int(input('Введите количество элементов стоки: '))
my_list = []
for i in range(number):
    new_el = input('Введите новый элемент: ')
    if new_el == 'True' or new_el == 'False':   # проверка является ли элемент булевым
        new_el = bool(new_el)
        print(type(new_el))
    elif new_el == 'None':  # проверка является ли тип данных элемента NoneType
        new_el = None
        print(type(new_el))
    elif new_el.isdigit():  # проверка является ли элемент числом
        new_el = int(new_el)
        print(type(new_el))
    my_list.append(new_el)
print(f'Список имеет вид: {my_list}')

try:
    for i in range(number):
        if my_list[i] == bool(my_list[i]) or my_list[i] == str(my_list[i]):
            raise OwnError('Список содержит неподходящие элементы')
except OwnError as e:
    print(e)







