# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
a = float(input('Enter first number: '))
b = float(input('Enter second number: '))

def func1 (a,b):
    try:
        c = a/b
    except ZeroDivisionError:
        return 'Division by zero is prohibited'

    return c
print(f'Result function: {func1(a,b)}')

