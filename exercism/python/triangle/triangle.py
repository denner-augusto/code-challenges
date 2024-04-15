"""
1. Check if it is a triangle
2. Check if it's equilateral
2. Check if it's isosceles 
2. Check if it's scalene
"""

def triangle_equality(sides: list) -> bool:
    return (sides[0] + sides[1] >= sides[2]) and (sides[1] + sides[2] >= sides[0]) and (sides[0] + sides[2] >= sides[1])

def is_triangle(sides: list) -> bool:
    return not(sides[0] == sides[1] == sides[2] == 0)

def equilateral(sides: list) -> bool:
    return sides[0] == sides[1] == sides[2] and is_triangle(sides) and triangle_equality(sides)


def isosceles(sides: list) -> bool:
    return (sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]) and is_triangle(sides) and triangle_equality(sides)


def scalene(sides: list) -> bool:
    return  sides[0] != sides[1] != sides[2] and sides[0] != sides[2] != sides[1] and is_triangle(sides) and triangle_equality(sides)
