#this is a calc which can do multible operations
#this bot uses python 3
print("Welcome to the calculator")

#create the multible function for the different operations
def calculate(x,y,operation):
    if operation == '+':
        return x+y
    elif operation == '-':
        return x-y
    elif operation == '*':
        return x*y
    elif operation == '/':
        return x/y
    else:
        return "Invalid input"