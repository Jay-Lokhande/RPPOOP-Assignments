class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def change_dimensions(self, new_length, new_width):
        self.length = new_length
        self.width = new_width

    def report_dimensions(self):
        return f"Length: {self.length}, Width: {self.width}"


aa =  Rectangle(2, 5)
aa.change_dimensions(5,4)
print(aa.report_dimensions())
