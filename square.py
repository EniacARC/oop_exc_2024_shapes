from rectangle import Rectangle


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