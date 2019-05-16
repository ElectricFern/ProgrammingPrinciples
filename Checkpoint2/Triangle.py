from Shape import Shape


class Triangle(Shape):

    # Class data none
    tri_area = (1/2)*Shape.tri_width*Shape.tri_height
    # Instance method
    def show_area(self):

        print("The area of the triangle is", self.tri_area)


# Are these meant to be here or in shape?
# I have had to recast these rather than call them from shape as the UML required INT but equation requires FLOAT
#     tri_width = 8
#     tri_width = float(tri_width)
#     tri_height = 6
#     tri_height = float(tri_height)


# Test code for the Triangle class

# triangle_1 = Triangle()
# triangle_1._colour = "blue"
# triangle_1._height = 6
# triangle_1._width = 8
#
# print("Testing variables, the colour is", triangle_1._colour)
# print("Testing variables, the height is", triangle_1._height)
# print("Testing variables, the width is", triangle_1._width)
# print("Testing function, the area is", triangle_1.show_area())
