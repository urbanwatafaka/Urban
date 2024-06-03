def pairs(n):
    pairs = []
    for a in range(1, n):
        for b in range(a, n):
            if n % (a + b) == 0 and a != b:
                pairs.append([a, b])
    return pairs

def pass_generator(pairs):
    password = ''
    for i in pairs:
        for number in i:
            password += str(number)
    return password
true_passwords = {3: 12,
4: 13,
5: 1423,
6: 121524,
7: 162534,
8: 13172635,
9: 1218273645,
10: 141923283746,
11: 11029384756,
12: 12131511124210394857,
13: 112211310495867,
14: 1611325212343114105968,
15: 1214114232133124115106978,
16: 1317115262143531341251161079,
17: 11621531441351261171089,
18: 12151811724272163631545414513612711810,
19: 118217316415514613712811910,
20: 13141911923282183731746416515614713812911}

n = int(input('Введите число:'))
pairs = pairs(n)
password = pass_generator(pairs)
if n in true_passwords:
    if true_passwords[n] == int(password):
        print('Ваш пароль:', password)
    else:
        print('Ошибка: неправильный пароль')
else:
    print('Ошибка: нет пароля для введенного числа')


