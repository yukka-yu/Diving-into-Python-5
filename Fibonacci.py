'''Создайте функцию генератор чисел Фибоначчи'''

F1 = 0
F2 = 1

def fibonacci(n):
    fib1 = 0
    fib2 = 1
    for count in range(n + 1):
        if count == 0:
            yield 0
        elif count == 1:
            yield 1
        else:
            yield fib1 + fib2
            fib1, fib2 = fib2, fib1 + fib2

for fib in fibonacci(5):
    print(fib)

print(*fibonacci(5))

            
    
        