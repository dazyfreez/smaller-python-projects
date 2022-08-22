#this will be a calculator in the consolein python 3
import math

print("Welcome to the calculator")

#create the multible function for the different operations
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

#create a variable for the user input
choice = input("Enter choice(1/2/3/4):")

