class Vehicle:
    vehicle_type = None
class Car:
    price = 1000000
    def __init__(self, horse_powers):
        self.horse_powers = horse_powers
    def engine_power(self, horse_powers):
        self.horse_powers = horse_powers
        return self.horse_powers
class Nissan(Vehicle, Car):
    def __init__(self, price, vehicle_type, horse_powers):
        self.price = super().price
        self.vehicle_type = super().vehicle_type
        self.horse_powers = super().engine_power
        print(f'Цена машины {self.price}, тип машины {self.vehicle_type}, мощность {self.horse_powers}')
car = Car(250)
car1 = Car.engine_power(car,250)
nissan = Nissan(1, 'машина', 250)
