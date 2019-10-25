# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def sumtwobiggest(a, b, c):
    if a == b and b == c:
        summ ='all three numbers is equal'
    elif a <= b and a <= c:
        summ = b + c
    elif b <= a and b <= c:
        summ = a + c
    else:
        summ = a + b
    return summ

print(sumtwobiggest(0, 0, 0))
