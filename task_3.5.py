# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
print('This program counts the sum of the numbers you entered.')
print("If you want to exit, enter the word - 'exit' instead of the number")

list1 = []
list2 = []
summ = 0
exit_code = 0


def sum_num(list1, summ, exit_code):
    summ1 = summ
    for i in range(0, len(list1)):
        if list1[i] == 'exit':
            exit_code = 1
            break
        else:
            summ1 = summ1 + int(list1[i])
            i = i + 1
    summ = int(summ1)
    return summ, exit_code


while True:
    if exit_code == 0:
        print('Enter any sequence of numbers. Separate the numbers with a space.')
        list1 = list((input()).split(' '))
        print(f'entered list: {list1}')
        summ, exit_code = sum_num(list1, summ, exit_code)
        print(f'Current amount: {summ}')
        continue
    else:
        print(f'The calculation is finished, the total amount: {summ}')
        break

