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
print("Select operation. The units are in cm")
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
    elif choice =="2":
        print("do you want to calculate the area of a square? type 1")
        print("do you want to calculate the perimeter of a square? type 2")
        print("do you want to calculate the side of a square? type 3")
        print("do you want to calculate the diagonal of a square? type 4")
        choice = input("Enter choice(1/2/3/4):")
        if choice == "1":
            side = int(input("Enter the side of the square: "))
            print("The area of the square is", square_area(side))
        elif choice == "2":
            side = int(input("Enter the side of the square: "))
            print("The perimeter of the square is", square_perimeter(side))
        elif choice == "3":
            perimeter = int(input("Enter the perimeter of the square: "))
            print("The side of the square is", square_side(perimeter))
        elif choice == "4":
            side = int(input("Enter the side of the square: "))
            print("The diagonal of the square is", square_diagonal(side))
        else:
            print("Invalid input")
    elif choice =="3":
        print("do you want to calculate the area of a triangle? type 1")
        print("do you want to calculate the perimeter of a triangle? type 2")
        print("do you want to calculate the height of a triangle? type 3")
        print("do you want to calculate the base of a triangle? type 4")
        print("do you want to calculate the side of a triangle? type 5")
        choice = input("Enter choice(1/2/3/4/5):")
        if choice == "1":
            base = int(input("Enter the base of the triangle: "))
            height = int(input("Enter the height of the triangle: "))
            print("The area of the triangle is", triangle_area(base, height))
        elif choice == "2":
            side1 = int(input("Enter the first side of the triangle: "))
            side2 = int(input("Enter the second side of the triangle: "))
            side3 = int(input("Enter the third side of the triangle: "))
            print("The perimeter of the triangle is", triangle_perimeter(side1, side2, side3))
        elif choice == "3":
            base = int(input("Enter the base of the triangle: "))
            area = int(input("Enter the area of the triangle: "))
            print("The height of the triangle is", triangle_height(base, area))
        elif choice == "4":
            height = int(input("Enter the height of the triangle: "))
            area = int(input("Enter the area of the triangle: "))
            print("The base of the triangle is", triangle_base(height, area))
        elif choice == "5":
            side2 = int(input("Enter the second side of the triangle: "))
            side3 = int(input("Enter the third side of the triangle: "))
            perimeter = int(input("Enter the perimeter of the triangle: "))
            print("The side of the triangle is", triangle_side1(side2, side3, perimeter))
        else:
            print("Invalid input")