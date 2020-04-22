import sys
import math

# Даны длины сторон треугольника. Вычислите площадь треугольника.
# Вводятся три положительных числа.

def get_area(vector):
    s = sum(vector)/2
    vector = (s - i for i in vector)
    v = 1
    for i in vector:
        v = v * i
    print(math.sqrt(v * s))

v = tuple(float(input()) for i in range(3))
get_area(v)