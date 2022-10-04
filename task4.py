# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
count = ""
number = int(input("Введите число :"))
while number != 0:
    count = str(number%2) + count
    number //=2
print(count)
