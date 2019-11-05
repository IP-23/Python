# Создание файла и добавление в него строк

file_new = open("HW_1.txt", 'w')   # открыть файл на запись, при этом удалить содержимое файла

while True:   # цикл добавления строк в файл
    string = input('Введите стороку: ')
    if string != '':
        file_new.write(string + '\n')
    else:
        break

file_new.close()
