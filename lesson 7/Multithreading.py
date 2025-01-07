import threading
import time


# Формула 1
def formula1(x):
    return x ** 2 - x ** 2 + x ** 4 - x ** 5 + x + x


# Формула 2
def formula2(x):
    return x + x


# Функция для вычислений по формуле 1
def compute_formula1(iterations):
    results = []
    for i in range(iterations):
        results.append(formula1(i))
    return results


# Функция для вычислений по формуле 2
def compute_formula2(iterations):
    results = []
    for i in range(iterations):
        results.append(formula2(i))
    return results


# Функция для выполнения вычислений и измерения времени
def compute_total(iterations):
    # Вычисление по формуле 1
    start_time = time.time()
    results1 = compute_formula1(iterations)
    formula1_time = time.time() - start_time

    # Вычисление по формуле 2
    start_time = time.time()
    results2 = compute_formula2(iterations)
    formula2_time = time.time() - start_time

    # Итоговое вычисление
    total_time = time.time() - start_time - formula1_time - formula2_time

    return formula1_time, formula2_time, total_time


# Функция для параллельных вычислений с использованием потоков
def parallel_computation(iterations):
    # Запуск потоков
    thread1 = threading.Thread(target=compute_formula1, args=(iterations,))
    thread2 = threading.Thread(target=compute_formula2, args=(iterations,))

    # Запуск потоков
    thread1.start()
    thread2.start()

    # Ожидание завершения потоков
    thread1.join()
    thread2.join()


# Главная функция для выполнения вычислений
def main():
    iterations_list = [10000, 100000]

    for iterations in iterations_list:
        print(f"Вычисления для {iterations} итераций:")

        # Запуск параллельных вычислений
        formula1_time, formula2_time, total_time = compute_total(iterations)

        print(f"Время для вычислений по формуле 1: {formula1_time:.4f} секунд")
        print(f"Время для вычислений по формуле 2: {formula2_time:.4f} секунд")
        print(f"Общее время вычислений: {total_time:.4f} секунд")
        print("-" * 30)


if __name__ == "__main__":
    main()
