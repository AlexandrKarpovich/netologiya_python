import multiprocessing
import time


# Формула 1
def formula1(x):
    return x**2 - x**2 + x**4 - x**5 + x + x

# Формула 2
def formula2(x):
    return x + x

# Функции для вычислений по формулам 1 и 2
def compute_formula1(iterations):
    results = []
    for i in range(iterations):
        results.append(formula1(i))
    return results

def compute_formula2(iterations):
    results = []
    for i in range(iterations):
        results.append(formula2(i))
    return results

# Параллельные вычисления с использованием процессов
def parallel_compute_formula1(iterations):
    return compute_formula1(iterations)

def parallel_compute_formula2(iterations):
    return compute_formula2(iterations)

# Функция для многопроцессных вычислений
def parallel_computation(iterations):
    # Создание процессов
    process1 = multiprocessing.Process(target=parallel_compute_formula1, args=(iterations,))
    process2 = multiprocessing.Process(target=parallel_compute_formula2, args=(iterations,))

    # Запуск процессов
    process1.start()
    process2.start()

    # Ожидание завершения процессов
    process1.join()
    process2.join()

# Главная функция для выполнения многопроцессных вычислений
def main():
    iterations_list = [10000, 100000]

    for iterations in iterations_list:
        print(f"Вычисления для {iterations} итераций:")

        # Запуск параллельных вычислений с процессами
        parallel_computation(iterations)

        print("Вычисления завершены")
        print("-" * 30)

if __name__ == "__main__":
    main()
