def hanoi(n, start, end, temp, moves):
    """
    Функция для решения задачи Ханойской башни с использованием рекурсии.

    :param n: количество колец
    :param start: стержень с которого переносим кольца
    :param end: стержень, на который переносим кольца
    :param temp: промежуточный стержень
    :param moves: список для хранения ходов
    """
    if n == 1:
        moves.append(f"Блин 1: Стержень {start} -> Стержень {end}.")
    else:
        hanoi(n - 1, start, temp, end, moves)  # Переместить n-1 колец на промежуточный стержень
        moves.append(f"Блин {n}: Стержень {start} -> Стержень {end}.")  # Переместить самое большое кольцо
        hanoi(n - 1, temp, end, start, moves)  # Переместить n-1 колец на целевой стержень


def get_initial_conditions():
    """
    Функция для получения начальных условий от пользователя (количество колец и стержней).

    :return: количество колец и количество стержней
    """
    while True:
        try:
            n = int(input("Введите количество колец: "))
            if n <= 0:
                print("Количество колец должно быть положительным числом!")
                continue
            return n
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите целое число.")


def print_solution(moves):
    """
    Функция для вывода решения на экран.

    :param moves: список ходов
    """
    print("\nРешение:")
    for move in moves:
        print(move)


def save_solution(moves):
    """
    Функция для записи решения в файл.

    :param moves: список ходов
    """
    with open("решение.txt", "w", encoding="utf-8") as file:
        for move in moves:
            file.write(move + "\n")


def main():
    # Получаем начальные условия
    n = get_initial_conditions()

    # Список для хранения ходов
    moves = []

    # Решаем задачу Ханойской башни
    hanoi(n, 1, 3, 2, moves)

    # Выводим решение на экран
    print_solution(moves)

    # Записываем решение в файл
    save_solution(moves)


if __name__ == "__main__":
    main()
