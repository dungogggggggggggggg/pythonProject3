# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
N = int(input('Задайте количество элементов:'))

def Fibonacci(n):
    if n in [1, 2]:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

def NegaFibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return -1
    else:
        return NegaFibonacci(n - 2) - NegaFibonacci(n - 1)

list = [0]
for e in range(1, N + 1):
    list.append(Fibonacci(e))
    list.insert(0, NegaFibonacci(e))
print(list)
