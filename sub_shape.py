import math
from shape import Shape
from typing_extensions import Self
from random import randint


class Rectangle(Shape):
    """
    A class representing a rectangle, inheriting from Shape.

    This class provides methods to calculate the area and perimeter
    of a rectangle. It also supports adding two rectangles together
    to create a new rectangle.

    :param color: The color of the rectangle.
    :type color: str
    :param width: The width of the rectangle.
    :type width: float
    :param length: The length of the rectangle.
    :type length: float
    """

    def __init__(self, color: str, width: float, length: float) -> None:
        """
        Initialize a Rectangle instance.

        :param color: The color of the rectangle.
        :type color: str
        :param width: The width of the rectangle.
        :type width: float
        :param length: The length of the rectangle.
        :type length: float
        :return: None
        """

        super().__init__(color)
        self._width = float(width)
        self._length = float(length)

    def calculate_area(self) -> float:
        """
        Calculate the area of the rectangle.

        :return: The area of the rectangle.
        :rtype: float
        """

        return self._width * self._length

    def calculate_perimeter(self) -> float:
        """
        Calculate the perimeter of the rectangle.

        :return: The perimeter of the rectangle.
        :rtype: float
        """

        return 2 * (self._width + self._length)

    def __add__(self, other: Self) -> Self:
        """
        Add two rectangles together to create a new rectangle.

        The width and length of the new rectangle are the sum of the widths
        and lengths of the original rectangles. The color of the new rectangle
        is randomly selected from one of the two rectangles.

        :param other: Another rectangle to add to this one.
        :type other: Rectangle
        :return: A new rectangle resulting from the addition.
        :rtype: Rectangle
        """

        if isinstance(other, Rectangle):
            new_width = self._width + other._width
            new_length = self._length + other._length
            new_color = self._color if randint(1, 2) == 1 else other._color
            return Rectangle(new_color, new_width, new_length)
        else:
            raise TypeError(f"Unsupported operand type(s) for +: 'Rectangle' and '{type(other).__name__}'")


class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle.

    Since a square is a special case of a rectangle where width equals
    length, this class uses the Rectangle's functionality with equal width
    and length.

    :param color: The color of the square.
    :type color: str
    :param width: The width of the square (also its length).
    :type width: float
    """

    def __init__(self, color: str, width: float) -> None:
        """
        Initialize a Square instance.

        :param color: The color of the square.
        :type color: str
        :param width: The width of the square.
        :type width: float
        :return: None
        """

        width = float(width)
        super().__init__(color, width, width)


class Circle(Shape):
    """
    Initialize a Circle instance.

    :param color: The color of the circle.
    :type color: str
    :param radius: The radius of the circle.
    :type radius: float
    :return: None
    """

    def __init__(self, color: str, radius: float):
        """
        Initialize a Circle instance.

        :param color: The color of the circle.
        :type color: str
        :param radius: The radius of the circle.
        :type radius: float
        :return: None
        """

        super().__init__(color)
        self.__radius = float(radius)

    def calculate_area(self) -> float:
        """
        Calculate the area of the circle.

        :return: The area of the circle.
        :rtype: float
        """

        return math.pi * self.__radius * self.__radius

    def calculate_perimeter(self) -> float:
        """
        Calculate the perimeter (circumference) of the circle.

        :return: The perimeter of the circle.
        :rtype: float
        """

        return 2 * math.pi * self.__radius
