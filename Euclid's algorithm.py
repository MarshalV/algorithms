# алгоритм Евклида

a = int(input())  # Запрашиваем у пользователя значение переменной a и преобразуем его в целое число.
b = int(input())  # Запрашиваем у пользователя значение переменной b и преобразуем его в целое число.

while b > 0:  # Начинается цикл, который продолжается до тех пор, пока значение переменной b больше 0.
    a, b = b, a % b  # Присваиваем переменной a значение переменной b, а переменной b — остаток от деления a на b.

print(a)  # После завершения цикла выводим значение переменной a, которое является наибольшим общим делителем (НОД) исходных чисел.
