#Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.


a = int(input("Введите целое число от 0 до 9: "))
print(f"Вы ввели число - {a}")
a = str(a)
b = int(a + a)
c = int(a + a + a)
a = int(a)
print(f"result -{a:>3},{b:>3},{c:>3}")
d = int(a + b + c)
print(f"Сумма чисел{a:>3},{b:>3},{c:>3}равна:{d:<3}")
