import math
from shape import Shape
from typing_extensions import Self
from random import randint


class Rectangle(Shape):
    def __init__(self, color: str, width: float, length: float) -> None:
        super().__init__(color)
        self._width = float(width)
        self._length = float(length)

    def calculate_area(self) -> float:
        return self._width * self._length

    def calculate_perimeter(self) -> float:
        return 2 * (self._width + self._length)

    def __add__(self, other: Self) -> Self:
        if isinstance(other, Rectangle):
            new_width = self._width + other._width
            new_length = self._length + other._length
            new_color = self._color if randint(1, 2) == 1 else other._color
            return Rectangle(new_color, new_width, new_length)
        else:
            return NotImplemented


class Square(Rectangle):
    def __init__(self, color: str, width: float) -> None:
        width = float(width)
        super().__init__(color, width, width)


class Circle(Shape):
    def __init__(self, color: str, radius: float):
        super().__init__(color)
        self.__radius = float(radius)

    def calculate_area(self) -> float:
        return math.pi * self.__radius * self.__radius

    def calculate_perimeter(self) -> float:
        return 2 * math.pi * self.__radius
