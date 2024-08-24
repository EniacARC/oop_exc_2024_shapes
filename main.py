from shape_container import ShapeContainer
from sub_shape import *


def main():
    my_container = ShapeContainer()
    my_container.generate(100)
    print("total area:", my_container.sum_area())
    print("total perimeter:", my_container.sum_perimeter())
    print("colors:", my_container.countColors())

    rect_a = Rectangle("White", 5, 4)
    rect_b = Square("Black", 4)
    rect_c = rect_a + rect_b
    print(rect_c.calculate_area())


if __name__ == '__main__':
    main()
