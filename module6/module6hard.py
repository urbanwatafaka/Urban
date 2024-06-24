import math


class Figure:
    sides_count = 0

    def __init__(self):
        self.__sides = []
        self.__color = []
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print('Некорректно введен цвет')

    def set_sides(self, *args):
        if self.__is_valid_sides(*args):
            self.__sides = list(args)
        else:
            print('Некорректное значение сторон')

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *args):
        for side in args:
            if not isinstance(side, (int)) or side <= 0:
                return False
        return True

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, okruj):
        super().__init__()
        self.__radius = okruj / (2 * 3.14)

    def det_square(self):
        return 3.14 * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self):
        super().__init__()

    def heron_formula(self):
        sides = self.get_sides()
        if len(sides) == 3:
            a, b, c = sides
            s = (a + b + c) / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            return area
        else:
            print('Недостаточно сторон для расчета площади треугольника')
            return None


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length):
        super().__init__()
        self.set_color(*color)
        self.set_sides(side_length)

    def set_sides(self, *args):
        if len(args) == 1 and super()._Figure__is_valid_sides(*args):
            self.__side_length = args[0]
        else:
            print('Некорректное значение сторон для куба')

    def get_side_length(self):
        return self.__side_length

    def get_volume(self):
        return self.__side_length ** 3



circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
circle1.set_sides(15)  # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
