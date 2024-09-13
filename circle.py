import math

from shape import Shape


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
