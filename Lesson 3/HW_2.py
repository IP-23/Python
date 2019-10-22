# Данные о пользователе


def data():
    """Возвращает данные о пользователе"""
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    birth_year = input('Введите год рождения: ')
    city = input('Введите город проживания: ')
    email = input('Введите email: ')
    ph_number = input('Введите номер телефона: ')
    user = str(f"Имя: {name}; Фамилия: {surname}; Год рождения: {birth_year}; Город проживания: {city}; Email: {email}; Номер телефона {ph_number}")
    return user


print(data())
