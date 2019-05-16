from Shape import Shape


class Rectangle(Shape):

    # Class data
    _border_size = int
    _perimeter = int
    rec_perimeter = Shape.rec_width+Shape.rec_width+Shape.rec_height+Shape.rec_height

    # Instance method
    def show_border_size(self):
        print("The border size of the rectangle is", self._border_size)

    def show_perimeter(self):
        print("the perimeter size of the rectangle is", self.rec_perimeter)


    # Are these meant to be here or in shape?
    # I have had to recast these rather than call them from shape as the UML required INT but equation requires FLOAT
    #     rec_width = 8
    #     rec_width = float(rec_width)
    #     rec_height = 6
    #     rec_height = float(rec_height)


# rectangle_1 = Rectangle()
# rectangle_1._border_size = 2
#
# print("Testing variable, the border size is", rectangle_1._border_size)
# print("Testing variable, the perimeter is", rectangle_1._perimeter)
