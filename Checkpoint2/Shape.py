
class Shape:

    # Class data for all
    _colour = str
    _height = int
    _width = int

    # Class data for Triangle, should this be here or uncommented in Triangle?
    tri_width = 8
    tri_width = float(tri_width)
    tri_height = 6
    tri_height = float(tri_height)
    # tri_area = (1/2)*tri_width*tri_height

    # Class data for Rectangle, should this be here or uncommented in Rectangle?
    rec_width = 8
    rec_width = float(rec_width)
    rec_height = 6
    rec_height = float(rec_height)
    # rec_perimeter = rec_width+rec_width+rec_height+rec_height

    # Instance method
    def show_colour(self):
        print("The colour of this shape is", self._colour)




# shape_1 = Shape()
# shape_1._colour = "red"
# shape_1._height = 6
# shape_1._width = 8
#
# print("Testing variable, the shape colour is", shape_1._colour)
