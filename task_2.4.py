str_1 = input('Enter other string with space between words: ')  # data input from user
# str_1 = ('Enter other string with space betweenebanana words')
print(f'String was entered: {str_1}')
str_1 = list(str_1.split(' '))

for i in range(len(str_1)):
    print(f'Word number {i + 1}: {(str_1[i])[:10]}')
    a = len(str_1[i])
    i += 1
    if a > 10:
        print(f'Word number {i} has been trimmed to 10 characters')
