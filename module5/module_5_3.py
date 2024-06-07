class Building:
    def __init__(self, floors_numbers, building_type):
        self.floors_numbers = floors_numbers
        self.building_type = building_type
    def __eq__(self, other):
        return self.floors_numbers == other.floors_numbers and self.building_type == other.building_type

building1 = Building(5, "Жилой")
building2 = Building(10, "Коммерческий")

print(f"Здание 1: {building1.floors_numbers} этажей, Тип: {building1.building_type}")
print(f"Здание 2: {building2.floors_numbers} этажей, Тип: {building2.building_type}")
print(building1 == building2)
print(building2 == building1)