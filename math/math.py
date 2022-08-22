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

while True:
    #create a variable for the user input
    choice = input("Enter choice(1/2/3/4):")

    if choice in ('1','2','3','4'):
        #create a variable for the user input
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == '1':
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice == '2':
            print(num1,"-",num2,"=",subtract(num1,num2))
        elif choice == '3':
            print(num1,"*",num2,"=",multiply(num1,num2))
        elif choice == '4':
            print(num1,"/",num2,"=",divide(num1,num2))
        #lets see if the user wants to continue
        next_task = input("Do you want to continue?(y/n)")
        if next_task == 'n':
            print("see you next time")
            break
    else:
        print("Invalid input")
        break

