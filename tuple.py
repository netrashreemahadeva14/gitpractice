#Tuple is ordered and immutable data structure in Python. It is used to store multiple items in a single variable. Tuples are defined by enclosing the items in parentheses ().
#Tuples are similar to lists, but they are immutable which means that we cannot change the values of a tuple after it is created. Tuples can contain duplicate values and can be of different data types.
#Tuples allows duplicate values and can be of different data types. Tuples are defined by enclosing the items in parentheses ().
#Tuples are indexed which means that each item in the tuple has a unique index value. The first item has an index of 0, the second item has an index of 1, and so on.
#Tuples can be created by using parentheses () or by using the tuple() constructor.


# fruits = ("apple", "banana", "cherry", "date", "elderberry",1,2,3,4,5)
# #Accessing tuple items by index
# print(fruits) #All values in the tuple
# print(fruits[1]) # values at index 1
# print(fruits[-1]) # values at index -1 (last item in the tuple)

numbers = (1, 2, 3, 4, 5,3)
print(numbers.count(3)) # returns the number of times 3 appears in the tuple
print(max(numbers)) # returns the maximum value in the tuple
print(min(numbers)) # returns the minimum value in the tuple