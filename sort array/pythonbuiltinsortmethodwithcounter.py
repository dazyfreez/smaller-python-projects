from array import array


array = [5, 4, 3, 2, 1, 3, 5, 6, 8, 10, 9, 7, 6, 5, 4, 3, 2, 1, 0]
print("Array before sorting: ", array)
print(sorted(array))
print(len(array))
print("do you want to count certain nubber in the array?")  
print("if yes, please enter the number")
print("if no, please enter 0")
number = int(input())
if number == 0:
    print("Array after sorting: ", sorted(array))
else:
    print("Array after sorting: ", sorted(array))
    print("the number of", number, "is", array.count(number))
    