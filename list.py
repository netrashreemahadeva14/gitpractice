#List is a collection which is ordered and changeable. Allows duplicate members.
#List can be separate data types and can be nested.
#List can be added, removed, and changed after it is created. It is defined by having values between square brackets [].
#It is ordered, mutable, and allows duplicate values. It is defined by having values between square brackets [].
#It is indexed which means that each item in the list has a unique index value. The first item has an index of 0, the second item has an index of 1, and so on.
#List can be created by using square brackets [] or by using the list() constructor.
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# #Accessing list items by index  
# print(fruits) #All values in the list
# print(fruits[1]) # values at index 1
# print(fruits[-1]) # values at index -1 (last item in the list)
# print(fruits[1:4]) # values from index 1 to 3 (4 is not included)

#Example to show mutability of list. We can change the value of an item in the list by accessing it by its index and assigning a new value to it.
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# print(fruits) #All values in the list
# fruits.append("blueberry")
# print(fruits) #All values in the list after changing the value at index 1
# fruits.remove("banana")
# print(fruits) #All values in the list after removing the value at index 1

# numbers = [1, 2, 3, 4, 5]
# for i in numbers:
#     print(i) # prints the value of i in each iteration.

#Find the sum of defined list
# numbers = [5, 10, 15, 20, 25]
# total = sum(numbers)
# print(total)

#Find the sum of defined list using for loop
numbers = [5, 10, 15, 20, 25]
for i in numbers:
    total = sum(numbers)
print(total)
