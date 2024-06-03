import random

member = 0
team_dict = {
    1: 'Real',
    2: 'Barsa',
    3: 'Газмяс3',
    4: 'Газмяс4',
    5: 'Газмяс5',
    6: 'Газмяс6',
    7: 'Газмяс7',
    8: 'Газмяс8',
    9: 'Газмяс9',
    10: 'Газмяс10',
    11: 'Газмяс11',
    12: 'Газмяс12'
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