import math
import sys
import matplotlib.pyplot as plt
import numpy as np

def sinus_cosinus():
    x = np.arange(0, 4* np.pi, 0.1)
    y = np.sin(x)
    z = np.cos(x)
    plt.plot(x,y,x,z)
    plt.show()
sinus_cosinus()
def show_function():
    x = np.arange(-10, 10, 0.1)
    y = 2*x**2 + 3*x + 1
    plt.plot(x,y)
    plt.show()
show_function()

def main():
    print("1. Sinus and cosinus")
    print("2. Show function")
    ex = input("Enter the number of the exercise you want to run: ")
    if ex == "1":
        sinus_cosinus()
    elif ex == "2":
            show_function()
    else:
        print("Invalid input")
        sys.exit()
main()

def intiger():
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    if x > y:
        print("The first number is bigger")
    elif x < y:
        print("The second number is bigger")
    else:
        print("The numbers are equal")

def pythagoras():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = math.sqrt(a**2 + b**2)
    print(c)

def motivation():
    print("You can do it! lets go!")

def x():
    print("x")
    
def main():
    print("1. Intiger")
    print("2. Pythagoras")
    print("3. Motivation")
    print("4. X")
    ex = input("Enter the number of the exercise you want to run: ")
    if ex == "1":
        intiger()
    elif ex == "2":
        pythagoras()
    elif ex == "3":
        motivation()
    elif ex == "4":
        x()
    else:
        print("Invalid input")
        sys.exit()