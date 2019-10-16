my_list = [7, 5, 3, 3]
print(f'Current raiting: {my_list}')
a = int(input('Please enter a new rating item: '))
i = 0

for i in range(len(my_list)):
    if i == len(my_list)-1:
        my_list.append(a)
    elif a > my_list[i]:
        my_list.insert(i,a)
        break
    elif a == my_list[i]:
        my_list.insert(i+1,a)
        break
print(my_list)


