# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month_year = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август',
              9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

while True:
    month = int(input('Enter the number of month: '))
    if month < 1 or month > 12:
        print("Entered number is incorrect. Let's true again")
        continue
    else:
        break

print(f'You entered the number {month}, it corresponds to the month of {month_year.get(month)}')

if month in winter:
    print(f'You have entered the winter month.')
elif month in spring:
    print(f'You have entered the spring month.')
elif month in summer:
    print(f'You have entered the summer month.')
else:
    print(f'You have entered the autumn month.')

