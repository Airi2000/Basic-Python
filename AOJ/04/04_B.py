import math


def circle_cir(r):
    return 2*r*math.pi


def circle_area(r):
    return r*r*math.pi


r = float(input())
print(circle_area(r), circle_cir(r))
