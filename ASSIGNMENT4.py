import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPainter, QPen, QColor, QPolygon
from PyQt5.QtCore import Qt, QPoint


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def change_dimensions(self, new_width, new_height):
        self.width = new_width
        self.height = new_height

    def report_dimensions(self):
        return f"Width: {self.width}, Height: {self.height}"


class Triangle:
    def __init__(self, points):
        self.points = points

    def area(self):
        x1, y1 = self.points[0].x(), self.points[0].y()
        x2, y2 = self.points[1].x(), self.points[1].y()
        x3, y3 = self.points[2].x(), self.points[2].y()
        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)

    def perimeter(self):
        side1 = self.points[0].distanceToPoint(self.points[1])
        side2 = self.points[1].distanceToPoint(self.points[2])
        side3 = self.points[2].distanceToPoint(self.points[0])
        return side1 + side2 + side3


class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 400)
        self.shape = None
        self.rectangle = None
        self.triangle = None
        self.points = []

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(Qt.black, 2.0))

        if self.shape == 'rectangle' and self.rectangle:
            self.draw_rectangle(painter)
        elif self.shape == 'triangle' and self.triangle:
            self.draw_triangle(painter)

    def mousePressEvent(self, event):
        if self.shape and event.button() == Qt.LeftButton:
            self.points.append(event.pos())
            if self.shape == 'rectangle':
                if len(self.points) == 2:
                    self.create_rectangle()
            elif self.shape == 'triangle':
                if len(self.points) == 3:
                    self.create_triangle()
            self.update()

    def create_rectangle(self):
        point1, point2 = self.points
        width = abs(point2.x() - point1.x())
        height = abs(point2.y() - point1.y())
        self.rectangle = Rectangle(width, height)

    def create_triangle(self):
        self.triangle = Triangle(self.points)

    def draw_rectangle(self, painter):
        point1, point2 = self.points
        rect = QRect(point1, point2)
        painter.drawRect(rect)

    def draw_triangle(self, painter):
        polygon = QPolygon(self.points)
        painter.drawPolygon(polygon)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.canvas = Canvas()
        self.rectangle_button = QPushButton("Rectangle")
        self.triangle_button = QPushButton("Triangle")

        self.rectangle_button.clicked.connect(self.set_rectangle_shape)
        self.triangle_button.clicked.connect(self.set_triangle_shape)

        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.rectangle_button)
        layout.addWidget(self.triangle_button)
        layout.addWidget(self.canvas)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def set_rectangle_shape(self):
        self.canvas.shape = 'rectangle'
        self.canvas.points = []
        self.canvas.rectangle = None
        self.canvas.triangle = None

    def set_triangle_shape(self):
        self.canvas.shape = 'triangle'
        self.canvas.points = []
        self.canvas.rectangle = None
        self.canvas.triangle = None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
