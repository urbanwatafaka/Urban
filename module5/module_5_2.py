class House:
    def __init__(self, floors_number):
        self.floors_number = floors_number
    def setNewNumberOfFloors(self, new_floor):
        self.floors_number = new_floor
my_house = House(2)
print("Этажей в здании:", my_house.floors_number)
my_house.setNewNumberOfFloors(3)
print("Измененное количество этажей в здании:", my_house.floors_number)