import math
from secrets import choice

print("Welcome to the geo_calculator")

#create a list of all the functions
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

# create a list of all the functions to choose from
print("Select operation.")
print("do you want to calculate something with a circle? type 1")   
print("do you want to calculate something with a square? type 2")   
print("do you want to calculate something with a triangle? type 3")
# create a variable for the user input
choice = input("Enter choice(1/2/3):")

if choice in ('1','2','3'):
    if choice =="1":
        print("do you want to calculate the area of a circle? type 1")
        print("do you want to calculate the circumference of a circle? type 2")
        print("do you want to calculate the diameter of a circle? type 3")
        print("do you want to calculate the radius of a circle? type 4")
        choice = input("Enter choice(1/2/3/4):")
        if choice == "1":
            radius = int(input("Enter the radius of the circle: "))
            print("The area of the circle is", circle_area(radius))
        elif choice == "2":
            radius = int(input("Enter the radius of the circle: "))
            print("The circumference of the circle is", circle_circumference(radius))
        elif choice == "3":
            radius = int(input("Enter the radius of the circle: "))
            print("The diameter of the circle is", circle_diameter(radius))
        elif choice == "4":
            diameter = int(input("Enter the diameter of the circle: "))
            print("The radius of the circle is", circle_radius(diameter))
        else:
            print("Invalid input")