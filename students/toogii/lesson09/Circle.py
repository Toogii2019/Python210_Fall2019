#!/usr/bin/env python3
from math import pi

class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    @property
    def diameter(self):
        return self.radius*2

    @property
    def area(self):
        return pi*self.radius**2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter/2

    @classmethod
    def from_diameter(cls,diameter):
        return cls(diameter/2)

    def __str__(self):
        return "Circle with radius = {}, diameter = {} , area = {}".format(self.radius, self.diameter, self.area)

    def __repr__(self):
        return str(__class__.__name__) + "(" + str(self.radius) + ")"

    def __add__(self, other):
        return Circle.from_diameter((self.radius+other.radius)*2)

    def __mul__(self, other):
        return Circle.from_diameter((self.radius*other)*2)

    def __rmul__(self,other):
        return Circle.from_diameter((self.radius*other)*2)

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __iadd__(self, other):
        return Circle.from_diameter((self.radius+other.radius)*2)

    def __imul__(self, other):
        return Circle.from_diameter((self.radius*other)*2)

class Sphere(Circle):
    def __repr__(self):
        return str(__class__.__name__) + "(" + str(self.radius) + ")"

    def __str__(self):
        return "Sphere with radius = {}, diameter = {} , area = {}".format(self.radius, self.diameter, self.area)
     
    @property
    def volume(self):
        return 4/3*pi*self.radius**3

    @property
    def area(self):
        return 4*pi*self.radius**2





