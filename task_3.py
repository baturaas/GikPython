# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.


a = int(input("Enter an integer between 0 and 9: "))
print(f"You entered a number: {a}")
a = str(a)
b = int(a + a)
c = int(a + a + a)
a = int(a)
print(f"Result: {a}, {b}, {c}")
d = int(a + b + c)
print(f"Summ of numbers {a}, {b}, {c} is equal to:{d}")
