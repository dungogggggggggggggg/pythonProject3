# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
from random import randint

N = int(input('Задайте длину списка:'))
numbers = []
for i in range(N):
    numbers.append(randint(1, 100))
print(numbers)
summa = 0
for i in range(1, len(numbers), 2):
        summa += numbers[i]
print(f'Сумма нечетных элементов: {summa}')
