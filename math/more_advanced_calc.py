#this is a calculator that can handle moren than 2 numbers
x=[]
amount=int(input("How many numbers?"))
operation=input("(*), (/), (+), (-)")
previous1 = 0
previous2=1
for i in range(amount):
    number=int(input("Number: "))
    x.append(number)
if operation == "+":
    for i in range(amount):
        previous1=x[i]+previous1
elif operation == "*":
    for i in range(amount):
        previous2=x[i]*previous2
elif operation == "-":
    for i in range(amount):
        previous1=x[i]-previous1
elif operation == "/":
    for i in range(amount):
        previous2=x[i]/previous2
if operation == "+" or operation == "-":
    print(previous1)
else:
    print(previous2)