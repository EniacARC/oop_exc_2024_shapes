import random
from sub_shape import *


class ShapeContainer:
    COLORS = ["Red", "Green", "Blue", "Yellow", "Pink", "White", "Black"]
    RANGE = (1, 10)
    ACCR = 2
    SHAPES = [type(Circle), type(Rectangle), type(Square)]

    def __init__(self) -> None:
        self.shapes = []

    @staticmethod
    def __generate_side() -> float:
        return round(random.uniform(ShapeContainer.RANGE[0], ShapeContainer.RANGE[1]),
                     ShapeContainer.ACCR)

    def generate(self, x: int) -> None:
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
        sum_area = 0.0
        for shape in self.shapes:
            sum_area += shape.calculate_area()
        return sum_area

    def sum_perimeter(self) -> float:
        sum_perimeter = 0.0
        for shape in self.shapes:
            sum_perimeter += shape.calculate_perimeter()
        return sum_perimeter

    def countColors(self) -> dict[str, int]:
        color_count = dict.fromkeys(ShapeContainer.COLORS, 0)

        for shape in self.shapes:
            color_count[shape.get_color()] += 1

        return color_count
