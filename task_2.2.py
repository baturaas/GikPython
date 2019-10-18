list1 = []
list2 = []
print('If you want to stop entering, type "end"')
while True:
    el = input("Enter element of list: ")
    if el != 'end':
        list1.append(el)
        continue
    else:
        break
print(f'You entered a list {list1} ,number of element in list {len(list1)}')

i = 1
a = len(list1)
while True:
    if i < a:
        list2.append(list1[i])
        list2.append(list1[i - 1])
        i = i + 2
        continue
    elif i == a:
        list2.append(list1[i-1])
        print(f'You list in which neighboring elements are swapped {list2}')
        break
    elif i > a:
        print(f'You list in which neighboring elements are swapped {list2}')
        break



