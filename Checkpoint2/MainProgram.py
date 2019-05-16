from Shape import Shape
from Rectangle import Rectangle
from Triangle import Triangle

def main():
    print("Welcome to the shape calculator")
    print("An instance of each of class follows: shape, rectangle, and triangle.")

# Shape instance

    shape_1 = Shape()
    shape_1._colour = "red"
    shape_1._height = 6
    shape_1._width = 8
    shape_1.show_colour()

    # print("Testing variable, the shape colour is", shape_1._colour)

# Rectangle instances

    rectangle_1 = Rectangle()
    rectangle_1._colour = "red"
    rectangle_1._border_size = 2
    rectangle_1.show_border_size()
    rectangle_1.show_perimeter()
    rectangle_1.show_colour()

    # print("Testing variable, the border size is", rectangle_1._border_size)
    # print("Testing variable, the perimeter is", rectangle_1._perimeter)

# Triangle instances

    triangle_1 = Triangle()
    triangle_1._colour = "red"
    triangle_1._height = 6
    triangle_1._width = 8
    triangle_1.show_area()
    triangle_1.show_colour()

    # print("Testing variables, the colour is", triangle_1._colour)
    # print("Testing variables, the height is", triangle_1._height)
    # print("Testing variables, the width is", triangle_1._width)
    # print("Testing function, the area is", triangle_1.show_area())


main()


