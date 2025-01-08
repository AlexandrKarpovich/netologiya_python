# Импортируем функцию из validate_car_number.py
from validate_car_number import validate_car_number
# Импортируем функцию
from remove_duplicates import remove_consecutive_duplicates

def main():
    # Примеры работы программы
    print(validate_car_number('А222BС96'))  # Номер А222ВС валиден. Регион: 96.
    print(validate_car_number('АБ22ВВ193'))  # Номер не валиден.

    # remove duplicates
    some_string = "Напишите функцию функцию, которая будет будет будет будет удалять все все все все последовательные повторы слов из из из из заданной строки строки при помощи регулярных выражений"
    # Удаляем последовательные повторы
    result = remove_consecutive_duplicates(some_string)

    print(result)

if __name__ == "__main__":
    main()
