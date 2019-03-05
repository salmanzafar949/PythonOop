class Polygon:

    def __init__(self, sides):
        self.sides = sides

    def Area(self,length):
        return length*length


class Square(Polygon):
    def __init__(self, permiter, sides):
        super().__init__(sides)
        self.permiter = permiter

class Triangle(Polygon):

    def Area(self, length, base):
        return 0.5*length*base

# t = Triangle(4)
s = Square(4,5)
print(s.permiter)
# print(isinstance(t, Polygon))
# print(issubclass(Triangle, Polygon))