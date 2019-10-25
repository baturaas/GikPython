# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

x = abs(float(input('Enter real positive number: ')))
y = int(input('Enter negative integer: '))
def exponentiation (x,y):
    expon = x ** y
    return expon
print(exponentiation(x,y))
