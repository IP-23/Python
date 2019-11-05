# Создание класса комплексных чисел.


class ComplexNumber:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):   # перегрузка операции сложения
        return ComplexNumber(self.a + other.a)

    def __mul__(self, other):   # перегрузка операции умножения
        return ComplexNumber(self.a * other.a)

    def __str__(self):  # преобразование объекта к строке для вывода
        return f'{self.a}'


if __name__ == '__main__':
    complex_number1 = ComplexNumber(1 + 2j)
    complex_number2 = ComplexNumber(2 - 1j)
    print(f'Сумма комплексных чисел: {complex_number1 + complex_number2}')
    print(f'Произведение комплексных чисел: {complex_number1 * complex_number2}')
