#this is in work, it is not finished yet

import math

def mitternachtsformel (a,b,c):
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    return x1, x2
def discriminant(a,b,c):
    return b**2 - 4*a*c
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
print(mitternachtsformel(a,b,c))
print(discriminant(a,b,c))
