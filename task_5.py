#Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.


income = int(input('Enter income of company: '))
expense = int(input('Enter expense of company: '))

if income > expense:
    print('You are Winner! Congratulate!')
    print(f'Profitability of the company is {income/expense:.3f}')
    workers = int(input('Enter the number of workers: '))
    print(f'Profit per employee is {income/workers:.2f}')
else:
    print('You are loser!')

