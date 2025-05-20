from functions.number_functions import *
from functions.validate_functions import *
from functions.convert_functions import *

def main():
    data = input()
    if validateUserInput(data):
        inputList = handleUserInput(data)
        print(f'Четные числа: {getEvenNumbers(inputList)}')
        print(f'Максимальное число: {getMax(inputList)}')
        print(f'Минимальное число: {getMin(inputList)}')
        print(f'Отсортированный список: {quickSort(inputList)}')
    else:
        print('Некорректный ввод: обнаружены последовательности символов, ' \
        'которые невозможно привести к int или float')

if __name__ == '__main__':
    main()