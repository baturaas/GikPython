income = int(input('Enter income of company: '))
expense = int(input('Enter expense of company: '))

if income > expense:
    print('You are Winner! Congratulate!')
    print(f'Profitability of the company is {income/expense:.3f}')
    workers = int(input('Enter the number of workers: '))
    print(f'Profit per employee is {income/workers:.2f}')
else:
    print('You are loser!')

