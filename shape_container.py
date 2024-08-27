import random
from sub_shape import *


class ShapeContainer:
    """
    A class to manage a collection of shapes and perform operations on them.

    This class allows for the generation of a collection of random shapes, 
    calculation of the total area and perimeter of the shapes, and counting 
    the occurrences of each color among the shapes.

    Class Attributes:
        COLORS (list of str): A list of possible colors for the shapes.
        RANGE (tuple of int): The range of possible side lengths for the shapes.
        ACCR (int): The number of decimal places for rounding the side lengths.
        SHAPES (list of type): A list of shape types that can be generated.
    """

    COLORS = ["Red", "Green", "Blue", "Yellow", "Pink", "White", "Black"]
    RANGE = (1, 10)
    ACCR = 2
    SHAPES = [type(Circle), type(Rectangle), type(Square)]

    def __init__(self) -> None:
        """
        Initialize a ShapeContainer instance.

        :return: None
        """

        self.shapes = []

    @staticmethod
    def __generate_side() -> float:
        """
        Generate a random side length within the predefined range.

        :return: A random side length rounded to the predefined number of decimal places.
        :rtype: float
        """

        return round(random.uniform(ShapeContainer.RANGE[0], ShapeContainer.RANGE[1]),
                     ShapeContainer.ACCR)

    def generate(self, x: int) -> None:
        """
        Generate a list of random shapes and store them in the container.

        Clears the existing shapes and generates a new list of shapes based on
        a specified number. Shapes are chosen randomly from the available types
        and assigned random colors and sizes.

        :param x: The number of shapes to generate.
        :type x: int
        :return: None
        """

        self.shapes.clear()
        for i in range(x):
            shape_type = random.choice(ShapeContainer.SHAPES)
            color = random.choice(ShapeContainer.COLORS)

            if shape_type == type(Circle):
                self.shapes.append(Circle(color, ShapeContainer.__generate_side()))
            elif shape_type == type(Rectangle):
                self.shapes.append(Rectangle(color, ShapeContainer.__generate_side(), ShapeContainer.__generate_side()))
            elif shape_type == type(Square):
                self.shapes.append(Square(color, ShapeContainer.__generate_side()))

    def sum_area(self) -> float:
        """
        Calculate the total area of all shapes in the container.

        :return: The total area of the shapes.
        :rtype: float
        """

        sum_area = 0.0
        for shape in self.shapes:
            sum_area += shape.calculate_area()
        return sum_area

    def sum_perimeter(self) -> float:
        """
        Calculate the total perimeter of all shapes in the container.

        :return: The total perimeter of the shapes.
        :rtype: float
        """

        sum_perimeter = 0.0
        for shape in self.shapes:
            sum_perimeter += shape.calculate_perimeter()
        return sum_perimeter

    def count_colors(self) -> dict[str, int]:
        """
        Count the occurrences of each color among the shapes in the container.

        :return: A dictionary where keys are colors and values are the counts of shapes of that color.
        :rtype: dict[str, int]
        """

        color_count = dict.fromkeys(ShapeContainer.COLORS, 0)

        for shape in self.shapes:
            color_count[shape.get_color()] += 1

        return color_count
