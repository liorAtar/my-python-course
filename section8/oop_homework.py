# Problem 1
# Fill in the Line class methods to accept coordinates as a pair of tuples
# and return the slope and distance of the line.

import math


class Line:

    def __init__(self, coor1: tuple, coor2: tuple):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1 = self.coor1[0]
        y1 = self.coor1[1]
        x2 = self.coor2[0]
        y2 = self.coor2[1]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def slope(self):
        x1 = self.coor1[0]
        y1 = self.coor1[1]
        x2 = self.coor2[0]
        y2 = self.coor2[1]
        return (y2 - y1) / (x2 - x1)


# EXAMPLE OUTPUT

coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)

print('distance', li.distance())
# 9.433981132056603

print('slope', li.slope())


# 1.6


# Problem 2
# Fill in the class

class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return math.pi * (self.radius ** 2) * self.height

    def surface_area(self):
        return 2 * math.pi * (self.radius ** 2) + 2 * math.pi * self.radius * self.height


# EXAMPLE OUTPUT
c = Cylinder(2, 3)

print('volume', c.volume())
# 56.52

print('surface area', c.surface_area())
# 94.2`
