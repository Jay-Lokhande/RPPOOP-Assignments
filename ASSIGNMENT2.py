class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)

    def report_sides(self):
        return f"Sides: {self.sides}"


class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__([length, width, length, width])

    def area(self):
        return self.sides[0] * self.sides[1]


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def area(self):
        return self.sides[0] ** 2


polygon = Polygon([2, 3, 4, 5])
print(polygon.perimeter())            # Output: 14
print(polygon.report_sides())         # Output: Sides: [2, 3, 4, 5]

rectangle = Rectangle(5, 10)
print(rectangle.area())               # Output: 50
print(rectangle.perimeter())          # Output: 30
print(rectangle.report_sides())       # Output: Sides: [5, 10, 5, 10]

square = Square(4)
print(square.area())                  # Output: 16
print(square.perimeter())             # Output: 16
print(square.report_sides())          # Output: Sides: [4, 4, 4, 4]
