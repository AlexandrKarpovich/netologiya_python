from datetime import datetime


def is_leap_year(year):
    try:
        datetime(year, 2, 29)
        return True
    except ValueError:
        return False


def main():
    while True:
        user_input = input('Введите год (или "exit" для выхода): ')
        if user_input.lower() == 'exit':
            print('Bye.')
            break
        year_input = int(user_input)
        if is_leap_year(year_input):
            print('Високосный год')
        else:
            print('Обычный год')


if __name__ == "__main__":
    main()