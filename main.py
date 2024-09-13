import math

from shape_container import ShapeContainer
from rectangle import Rectangle
from square import Square
from circle import Circle


def test_rectangle() -> None:
    """
    Tests for the Rectangle class.

    :return: None
    """

    rect1 = Rectangle("Red", 3.0, 4.0)
    rect2 = Rectangle("Blue", 5.0, 6.0)

    # Test color
    assert rect1.get_color() == "Red"

    # Test area calculation
    assert rect1.calculate_area() == 12.0

    # Test perimeter calculation
    assert rect1.calculate_perimeter() == 14.0

    # Test color change
    rect1.set_color("Blue")
    assert rect1.get_color() == "Blue"

    # Test addition of rectangles
    combined_rect = rect1 + rect2

    # Verify the dimensions of the resulting rectangle
    assert math.isclose(combined_rect._width, 8.0, rel_tol=1e-9)
    assert math.isclose(combined_rect._length, 10.0, rel_tol=1e-9)

    # Verify that the color is one of the original colors
    assert combined_rect.get_color() in ["Blue", "Blue"]

    # Test addition with incompatible type
    try:
        rect1 + "Some Text"
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError wasn't raised!"


def test_circle():
    """
    Tests for the Circle class.

    :return: None
    """

    circ = Circle("Yellow", 7.0)

    # Test color
    assert circ.get_color() == "Yellow"

    # Test area calculation
    assert circ.calculate_area() == math.pi * 49.0

    # Test perimeter calculation
    assert circ.calculate_perimeter() == 2 * math.pi * 7.0


def test_shape_container():
    """
    Tests for the ShapeContainer class.

    :return: None
    """

    shape_num = 10

    container = ShapeContainer()

    # Generate shapes
    container.generate(shape_num)

    # Test sum_area and sum_perimeter with generated shapes
    area_sum = container.sum_area()
    perimeter_sum = container.sum_perimeter()

    # Check if sums are positive
    assert area_sum > 0
    assert perimeter_sum > 0

    # Test color count
    color_count = container.count_colors()

    # check all colors are present
    assert sorted(ShapeContainer.COLORS) == sorted(color_count.keys())
    # Check if color counts are correct and non-negative and in range
    for color in ShapeContainer.COLORS:
        assert 0 <= color_count[color] <= shape_num


def main():
    my_container = ShapeContainer()
    my_container.generate(100)
    print("total area:", my_container.sum_area())
    print("total perimeter:", my_container.sum_perimeter())
    print("colors:", my_container.count_colors())

    rect_a = Rectangle("White", 5, 4)
    rect_b = Square("Black", 4)
    rect_c = rect_a + rect_b
    print(rect_c.calculate_area())


if __name__ == '__main__':
    test_rectangle()
    test_circle()
    test_shape_container()
    main()
