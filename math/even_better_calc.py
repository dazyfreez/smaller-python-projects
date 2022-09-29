#this is in work, it is not finished yet

import math

def mitternachtsformel (a,b,c):
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    return x1, x2
def discriminant(a,b,c):
    return b**2 - 4*a*c
    if discriminant(a,b,c) > 0:
        print("The equation has two solutions")
    elif discriminant(a,b,c) == 0:
        print("The equation has one solution")
    else:
        print("The equation has no solution")
def main():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    print("The solutions are: ", mitternachtsformel(a,b,c))
    print("The discriminant is: ", discriminant(a,b,c))