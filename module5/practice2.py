class House:
    def __init__(self):
        self.number_of_floors = 0
    def setNewNumberOfFloors(self, floors):
        self.number_of_floors = floors
        print(self.number_of_floors)

house = House()
house.setNewNumberOfFloors(12)