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