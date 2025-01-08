from functools import lru_cache

# 1. Рекурсивная функция без мемоизации
def min_breaks_recursive(n, m):
    # Базовые случаи
    if n == 1 and m == 1:
        return 0
    elif n == 1:
        return m - 1
    elif m == 1:
        return n - 1
    else:
        # Рекурсивный случай
        return min(min_breaks_recursive(n-1, m) + m, min_breaks_recursive(n, m-1) + n)

# 2. Рекурсивная функция с мемоизацией
@lru_cache(None)  # Без ограничения на количество кэшируемых результатов
def min_breaks_memoized(n, m):
    # Базовые случаи
    if n == 1 and m == 1:
        return 0
    elif n == 1:
        return m - 1
    elif m == 1:
        return n - 1
    else:
        # Рекурсивный случай
        return min(min_breaks_memoized(n-1, m) + m, min_breaks_memoized(n, m-1) + n)


def main():
    # Примеры для рекурсивной функции без мемоизации
    print("Без мемоизации:")
    print(min_breaks_recursive(2, 3))  # Должно вывести 5
    print(min_breaks_recursive(3, 3))  # Должно вывести 8
    print(min_breaks_recursive(1, 1))  # Должно вывести 0

    # Примеры для рекурсивной функции с мемоизацией
    print("\nС мемоизацией:")
    print(min_breaks_memoized(2, 3))  # Должно вывести 5
    print(min_breaks_memoized(3, 3))  # Должно вывести 8
    print(min_breaks_memoized(1, 1))  # Должно вывести 0


if __name__ == "__main__":
    main()
