#Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

total_sec = int(input('Введите любое количество секунд: '))
print(f"Вы ввели {total_sec} секунд.")

sec_res = total_sec % 60
if sec_res < 10:
    sec_res = '0'+str(sec_res)
min_res = int((total_sec % 3600)/60)
if min_res < 10:
    min_res = '0'+str(min_res)
hour_res = int(total_sec//3600)
if hour_res < 10:
    hour_res = '0'+str(hour_res)

print(f"Введенное Вами количество секунд содержит часов, минут, секунд: {hour_res}:{min_res}:{sec_res}")