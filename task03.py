'''Создайте функцию генератор чисел Фибоначчи'''

def fibonacci(n):
    fib_list = [0, 1]
    for i in range(2, n + 1):
        number = fib_list[i - 1] + fib_list[i - 2]
        fib_list.append(number)
    return fib_list[-1]


print(f'Fibonacci(10) = {fibonacci(10)}')    
