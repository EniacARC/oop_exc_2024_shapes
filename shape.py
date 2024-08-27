from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class representing a geometric shape.

    This class provides a template for all shapes by defining methods
    to calculate the area and perimeter. Additionally, it manages the
    color attribute of the shape.

    :param color: The color of the shape.
    :type color: str
    """

    def __init__(self, color: str) -> None:
        """
        Initialize the Shape with a specific color.

        :param color: The color of the shape.
        :type color: str
        :return: None
        """

        self._color = color

    def get_color(self) -> str:
        """
        Get the color of the shape.

        :return: The color of the shape.
        :rtype: str
        """

        return self._color

    def set_color(self, color: str) -> None:
        """
        Set the color of the shape.

        :param color: The new color of the shape.
        :type color: str
        :return: None
        """

        self._color = color

    @abstractmethod
    def calculate_area(self) -> float:
        """
        Calculate the area of the shape.

        This method must be implemented by subclasses.

        :return: The area of the shape.
        :rtype: float
        """

        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        """
        Calculate the perimeter of the shape.

        This method must be implemented by subclasses.

        :return: The perimeter of the shape.
        :rtype: float
        """

        pass
