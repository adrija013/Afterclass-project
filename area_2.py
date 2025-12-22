class Polygon:
    def area(self):
        print("Area method should be implemented by child classes")



class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height



class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


triangle = Triangle(12, 5)
rectangle = Rectangle(5, 4)

print("Area of Triangle:", triangle.area())
print("Area of Rectangle:", rectangle.area())