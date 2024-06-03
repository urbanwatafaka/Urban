import random

member = 0
team_dict = {
    1: 'МС',
    2: 'Арсенал',
    3: 'Барселона',
    4: 'Бавария',
    5: 'Реал Мадрид',
    6: 'Челси',
    7: 'ПСЖ',
    8: 'АТМ',
    9: 'Ливерпуль',
    10: 'Интер',
    11: 'Милан',
    12: 'Юве'
}


while True:
    if not team_dict:  # Проверка, чтобы избежать ошибки при пустом словаре
        break

    a = random.choice(list(team_dict.keys()))
    print(team_dict[a])
    team_dict.pop(a)
    member += 1

    if member == 3:
        break
input('Нажми Enter для выхода')
