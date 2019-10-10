# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

while True:
    number = input(f'Введите любой целое положительное число: ')
    try:
        int(number)
    except ValueError:
        print('Введенные Вами данные не соответствуют условию, повторите ввод')
        continue
    if number < '0':
        print('Введено отрицательное значение. Повторите ввод')
        continue
    else:
        print('Введенное вами число соответствует заданным параметрам')
        break
print(number)
number = int(number)
max_num = int(0)
num = int(0)

while True:
    print(number,num,max_num)
    num = number % 10

    if number < 10:
        if max_num < number:
            print(f'Самая большая цифва из введенного вами числа - {number}')
            break
        else:
            print(f'Самая большая цифва из введенного вами числа - {max_num}')
            break
    number = int((number - num) / 10)

    if max_num <= num:
        max_num = num
        continue
    else:
        continue
