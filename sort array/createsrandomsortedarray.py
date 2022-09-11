import numpy as np
print("how many digits should the array have")
x = int(input())    # number of digits in the array
array = np.random.randint(1,1000,(4, 5)) # random numpy array of shape (4,5)
print("first array", array) # print the array                                        
print("Array before sorting: ", array) # print the array before sorting
print(sorted(array)) # print the array after sorting 
print("do you want to count certain nubber in the array?") 
print("if yes, please enter the number")
print("if no, please enter 0")
number = int(input())
if number == 0:
    print("Array after sorting: ", sorted(array))
    print("do you want to reverse sort the array?")
    print("if yes, please enter 1")
    print("if no, please enter 0")
    reverse = int(input())
    if reverse == 1:
        print("Array after reverse sorting: ", sorted(array, reverse=True))
else:
    print("Array after sorting: ", sorted(array))
    print("the number of", number, "is", array.count(number))
    print("do you want to reverse sort the array?")
    print("if yes, please enter 1")
    print("if no, please enter 0 x")
    reverse = int(input())
    if reverse == 1:
        print("Array after reverse sorting: ", sorted(array, reverse=True))
    else:
        print("Array after reverse sorting: ", sorted(array))
        print("the number of", number, "is", array.count(number))
# array = [5, 4, 3, 2, 1, 3, 5, 6, 8, 10, 9, 7, 6, 5, 4, 3, 2, 1, 0]    # array to be sorted
# print("Array before sorting: ", array) # print the array before sorting
# print(sorted(array)) # print the array after sorting
# print("Array after sorting: ", sorted(array)) # print the array after sorting
# print("the number of 3 is", array.count(3)) # print the number of 3 in the array
# ur done
