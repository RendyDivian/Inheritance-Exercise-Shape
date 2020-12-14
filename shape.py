import math

class Shape:
    def __init__(self, color="Green", filled=True):
        self.color = color
        self.filled = filled

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def isFilled(self):
        if self.color == "":
            self.filled = False
            return "not filled"
        else:
            self.filled = True
            return "is filled"

    def setFilled(self, filled):
        self.filled = filled

    def __str__(self):
        return f"A shape with a color of {self.color} and {Shape.isFilled(self)}"

class Circle(Shape):
    def __init__(self, color, filled, radius=1.0):
        super().__init__(color, filled)
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius

    def get_area(self):
        area = math.pi * (self.get_radius() ** 2)
        return area

    def get_perimeter(self):
        perimeter = math.pi * 2 * self.get_radius()
        return perimeter

    def to_string(self):
        return f'''A circle with radius {self.get_radius()}, which is a subclass of {super().to_string()}'''

class Rectangle(Shape):
    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def get_length(self):
        return self.length

    def set_length(self, length):
        self.length = length

    def get_area(self):
        area = self.width * self.length
        return area

    def get_perimeter(self):
        perimeter = 2 * (self.width + self.length)
        return perimeter

    def to_string(self):
        return f'''A {self.color} rectangle has a width and length of {self.width} and {self.length} respectively.
        An area of the rectangle is {print(self.get_area())} and its perimeter is {print(self.get_perimeter())}.'''

class Square(Rectangle):
    def __init__(self, color, filled, side):
        super().__init__(color, filled, side)

    def get_side(self):
        return self.length

    def set_side(self, side):
        self.width = side
        self.length = side

    def set_width(self, side):
        self.width = side

    def set_length(self, side):
        set.length = side

    def to_string(self):
        return f'A Square with side {self.length}, which si a subclass of {super().to_string()}'
