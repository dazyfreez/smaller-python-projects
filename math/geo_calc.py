import math

print("Welcome to the calculator")

def circle_area(radius):
    return math.pi * radius**2
def circle_circumference(radius):
    return 2 * math.pi * radius
def circle_diameter(radius):
    return 2 * radius
def circle_radius(diameter):   
    return diameter / 2
def square_area(side):
    return side**2
def square_perimeter(side):
    return 4 * side
def square_side(perimeter):
    return perimeter / 4
def square_diagonal(side):
    return math.sqrt(2) * side
def triangle_area(base, height):
    return (base * height) / 2
def triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3
def triangle_height(base, area):
    return (2 * area) / base
def triangle_base(height, area):
    return (2 * area) / height
def triangle_side1(side2, side3, perimeter):
    return perimeter - side2 - side3
