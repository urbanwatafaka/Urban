class Building:
    total = 0
    def __init__(self):
        Building.total+=1
for i in range(40):
    buinding = Building()
    print(buinding)
print('Всего зданий сделано: ', Building.total)