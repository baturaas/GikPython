# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

"""f_name = 'Vasya'
s_name = 'Pupkin'
b_year = 1488
r_city = 'Bobryisk'
phone = 88005553535
email = 'vot_ty@dikaya.ru'
"""


def func_2(f_name, s_name, b_year, r_city, phone, email):
    str1 = f_name + ' ' + s_name + ' ' + b_year + ' ' + r_city + ' ' + phone + ' ' + email # stubit but it works(
    # str1 = ' '.join(f_name, s_name, b_year, r_city, phone, email)

    return str1


print(func_2(f_name='Vasya', s_name='Pupkin', b_year='1488', r_city='Bobryisk', phone='88005553535',email='vot_ty@dikaya.ru'))
