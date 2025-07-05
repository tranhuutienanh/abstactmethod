from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return int(self.radius) ^ 2 * 3.14
    
    def perimeter(self):
        return int(self.radius) * 2 * 3.14


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return int(self.length) * int(self.width)
    
    def perimeter(self):
        return (int(self.length) + int(self.width)) * 2


class Square(Shape):
    def __init__(self, edge):
        self.edge = edge

    def area(self):
        return int(self.edge) ^ 2
    
    def perimeter(self):
        return int(self.edge) * 4

class Rectangle(Shape):
    def __init__(self, bottom_edge, height, edge):
        self.bottom_edge = bottom_edge
        self.height = height
        self.edge = edge

    def area(self):
        return int(self.bottom_edge) * int(self.height) / 2
    
    def perimeter(self):
        return int(self.edge) * 4







