class House:
    def __init__(self, street, number):
        self.street = street
        self.number = number
        self.age = 0

    def build(self):
        print('Дом на улице', self.street, 'под номером', str(self.number), 'построен')

    def age_of_house(self, year):
        self.age += year
        print('Возраст дома', self.age)

class ProspectHouse(House):
    def __init__(self, prospect, number):
        super().__init__(self,number)
        self.prospect = prospect

prhouse = ProspectHouse('Ленина', 43)
print(prhouse.prospect, prhouse.number)