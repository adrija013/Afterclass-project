class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


triangle = Triangle(10, 5)
rectangle = Rectangle(8, 4)

print("Area of Triangle:", triangle.area())
print("Area of Rectangle:", rectangle.area())