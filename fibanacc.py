# генератор Фибаначчи

"""def fibonacci(n):  # Объявляем функцию fibonacci с одним параметром n.
    a, b = 1, 1  # Инициализируем начальные значения последовательности Фибоначчи.
    for i in range(n):  # Запускаем цикл, который будет повторяться n раз.
        yield a  # Возвращаем текущее значение последовательности Фибоначчи.
        a, b = b, a + b  # Обновляем значения переменных a и b для следующего шага последовательности.

data = list(fibonacci(100))  # Создаём список из первых 100 чисел последовательности Фибоначчи.
print(data)  # Выводим этот список на экран."""


import numba


@numba.jit
def fibonacci(n):
    fib_sequence = [1, 1]  # Начальные значения последовательности
    while len(fib_sequence) < n:  # Пока длина последовательности меньше n
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])  # Добавляем следующее число в последовательность
    return fib_sequence

try:
    from numba import cuda
    device = cuda.get_current_device()  # Получаем информацию о текущем устройстве (если есть GPU)
    print("Using GPU:", device.name)
    data = fibonacci(1000)  # Вызываем функцию fibonacci на GPU
except:
    print("No GPU available. Using CPU.")
    data = fibonacci(100)  # Вызываем функцию fibonacci на CPU

print(data)