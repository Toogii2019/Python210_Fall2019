#!/usr/bin/env python3
from math import pi
from Circle import Circle,Sphere
import unittest
import random

class TestCircle(unittest.TestCase):

    def test_ing_add(self):
        i = 0
        while i < 10:
            i = random.randint(0,50)
            j = random.randint(51,100)
            self.assertEqual(Circle(i) + Circle(j), Circle(i+j))
            i += 1
    def test_ing_str(self):
        i = random.randint(0,50)
        self.assertEqual(str(Circle(i)), "Circle with radius = {}, diameter = {} , area = {}".format(str(Circle(i).radius), str(Circle(i).diameter), str(Circle(i).area)))


    def test_ing_repr(self):
        i = random.randint(0,50)
        self.assertEqual(repr(Circle(i)), 'Circle({})'.format(i))

    def test_ing_mul(self):
        i = random.randint(0,50)
        j = random.randint(51,100)
        self.assertEqual(Circle(i)*j, Circle(Circle(i).radius*j))  

    def test_ing_rmul(self):
        i = random.randint(0,50)
        j = random.randint(51,100)
        self.assertEqual(j*Circle(i), Circle(Circle(i).radius*j))   

    def test_ing_lt(self):
        i = random.randint(0,10)       
        j = random.randint(0,10)
        self.assertEqual(Circle(i).radius < Circle(j).radius, Circle(i) < Circle(j))

    def test_ing_gt(self):
        i = random.randint(0,50)       
        j = random.randint(51,100)
        self.assertEqual(Circle(i).radius > Circle(j).radius, Circle(i) > Circle(j))

    def test_ing_eq(self):
        i = random.randint(0,3)       
        j = random.randint(0,3)
        self.assertEqual(Circle(i).radius == Circle(j).radius, Circle(i) == Circle(j))

    def test_ing_iadd(self):
        i = 0
        while i < 10:
            i = random.randint(0,50)
            j = random.randint(51,100)
            c1 = Circle(i)
            c2 = Circle(j)
            c1+=c2
            self.assertEqual(eval(repr(c1)), Circle(i+j))
            i += 1

    def test_ing_imul(self):
        i = 0
        while i < 10:
            i = random.randint(0,50)
            j = random.randint(51,100)
            c1 = Circle(i)
            c1*=j
            self.assertEqual(eval(repr(c1)), Circle(i*j))
            i+=1

    def test_ing_classmethod(self):
            i = random.randint(0,50)
            j = random.randint(51,100)
            c1 = Circle.from_diameter(i)
            self.assertEqual(eval(repr(c1)), Circle(i/2))

    def test_ing_area(self):
        self.assertEqual(Circle(5).area, pi*Circle(5).radius**2 )


    def test_ing_sphere_add(self):
        i = 0
        while i < 10:
            i = random.randint(0,50)
            j = random.randint(51,100)
            self.assertEqual(Sphere(i) + Sphere(j), Sphere(i+j))
            i += 1
    def test_ing_sphere_str(self):
        i = random.randint(0,50)
        self.assertEqual(str(Sphere(i)), "Sphere with radius = {}, diameter = {} , area = {}".format(str(Sphere(i).radius), str(Sphere(i).diameter), str(Sphere(i).area)))


    def test_ing_sphere_repr(self):
        i = random.randint(0,50)
        self.assertEqual(repr(Sphere(i)), 'Sphere({})'.format(i))

    def test_ing_sphere_mul(self):
        i = random.randint(0,50)
        j = random.randint(51,100)
        self.assertEqual(Sphere(i)*j, Sphere(Sphere(i).radius*j))  

    def test_ing_sphere_rmul(self):
        i = random.randint(0,50)
        j = random.randint(51,100)
        self.assertEqual(j*Sphere(i), Sphere(Sphere(i).radius*j))   

    def test_ing_sphere_lt(self):
        i = random.randint(0,10)       
        j = random.randint(0,10)
        self.assertEqual(Sphere(i).radius < Sphere(j).radius, Sphere(i) < Sphere(j))

    def test_ing_sphere_gt(self):
        i = random.randint(0,50)       
        j = random.randint(51,100)
        self.assertEqual(Sphere(i).radius > Sphere(j).radius, Sphere(i) > Sphere(j))

    def test_ing_sphere_eq(self):
        i = random.randint(0,3)       
        j = random.randint(0,3)
        self.assertEqual(Sphere(i).radius == Sphere(j).radius, Sphere(i) == Sphere(j))

    def test_ing_sphere_iadd(self):
        i = 0
        while i < 10:
            i = random.randint(0,50)
            j = random.randint(51,100)
            c1 = Sphere(i)
            c2 = Sphere(j)
            c1+=c2
            self.assertEqual(eval(repr(c1)), Sphere(i+j))
            i += 1

    def test_ing_sphere_imul(self):
        i = 0
        while i < 10:
            i = random.randint(0,50)
            j = random.randint(51,100)
            c1 = Sphere(i)
            c1*=j
            self.assertEqual(eval(repr(c1)), Sphere(i*j))
            i+=1

    def test_ing_sphere_classmethod(self):
            i = random.randint(0,50)
            j = random.randint(51,100)
            c1 = Sphere.from_diameter(i)
            self.assertEqual(eval(repr(c1)), Sphere(i/2))

    def test_ing_sphere_volume(self):
        self.assertEqual(Sphere(5).volume, 4/3*pi*Sphere(5).radius**3)

    def test_ing_sphere_area(self):
        self.assertEqual(Sphere(5).area, 4*pi*Sphere(5).radius**2)

    def test_ing_sphere_area(self):
        error = AttributeError("can't set attribute")
        try:
            Sphere(5).area = 10
        except AttributeError as result:
            self.assertEqual(str(result), str(error))
        

if __name__ == '__main__':
    unittest.main()







