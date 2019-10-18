a = int(input('Enter number the goods which you want add to list: '))
a = a + 1
i = 1
list_goods = []
prod_desc = []
total_analitics = []
analytics = []
for i in range(1, a):
    prod_desc = dict({'name': input(f'Enter the name {i}: '), 'price': input(f'Enter the price {i}: '), 'amount': input(f'Enter amount goods {i}: '), 'unit': input(f'Enter the unit {i}: ')})
    list_goods.append((i, prod_desc))
    analytics = dict({'name: ': prod_desc.get('name'), 'price: ': prod_desc.get('price'), 'amount: ': prod_desc.get('amount'), 'unit: ': prod_desc.get('unit')})
    total_analitics.append((i,analytics))
    i += 1

print(list_goods)
print(type(list_goods))
print(total_analitics)
