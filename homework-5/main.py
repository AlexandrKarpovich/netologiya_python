from datetime import datetime


def convert_date(date_string):
    # Список форматов для конвертации
    formats = [
        ("%A, %B %d, %Y", "The Moscow Times"),  # Wednesday, October 2, 2002
        ("%A, %d.%m.%y", "The Guardian"),  # Friday, 11.10.13
        ("%A, %d %B %Y", "Daily News")  # Thursday, 18 August 1977
    ]

    for date_format, newspaper in formats:
        try:
            # Пытаемся преобразовать строку в дату с использованием формата
            date_obj = datetime.strptime(date_string, date_format)
            return date_obj
        except ValueError:
            # Если формат не подошел, пробуем следующий формат
            continue

    # Если ни один формат не подошел
    raise ValueError(f"Дата не соответствует известным форматам")


def main():
    print("Введите даты в формате, используемом в газетах:")
    print("Пример 1: Wednesday, October 2, 2002 (The Moscow Times)")
    print("Пример 2: Friday, 11.10.13 (The Guardian)")
    print("Пример 3: Thursday, 18 August 1977 (Daily News)")
    print("Для завершения программы введите 'exit'.")

    while True:
        # Получаем ввод пользователя
        user_input = input("Введите дату: ")

        # Если введено 'exit', завершить программу
        if user_input.lower() == 'exit':
            print("Завершение программы.")
            break

        try:
            # Пытаемся конвертировать дату
            converted_date = convert_date(user_input)
            print(f"Конвертированная дата: {converted_date}")
        except ValueError as e:
            print(e)  # Выводим сообщение об ошибке


if __name__ == "__main__":
    main()
