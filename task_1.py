name = str(input('Какое твое имя? '))
print(f'Привет, {name}!')
year_old = int(input('Сколько тебе лет? '))
if year_old < 0:
    print(f"{n} ты из будующего, никуда не уходи, за тобой уже выехали!")
born_year = 2019 - year_old
print(f'Ты родился в {born_year} году')
f = str(input('Хочешь продолжить разговор? y/n '))
if 'n' != f:
    print('А я не хочу! Досвидос')
else:
    print(f'Ну и ладно,{name}, не очень-то и хотелось!')
