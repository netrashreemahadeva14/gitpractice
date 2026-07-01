#num1 = input("Enter first number: ")
#num2 = input("Enter second number: ") #input() function takes input from user in string format. So, we need to convert it into integer using int() function.
#print("The sum of two numbers is: ", int(num1) + int(num2))

#typecasting is the process of converting one data type into another data type. In Python, we can use the int(), float(), str() functions to convert data types.
#conversion of string to integer
# age = "22"
# print(type(age)) # <class 'str'>
# age = int(age) # converting string to integer
# print(type(age)) # <class 'int'>
# #conversion of float to integer
# #This removes the decimal part and returns the integer part of the float value. Does not round the value to the nearest integer.
# height = 5.9
# print(type(height)) # <class 'float'>
# height = int(height) # converting float to integer
# print(type(height)) # <class 'int'>
# #conversion of integer to string
# num = 10
# print(type(num)) # <class 'int'>
# num = str(num) # converting integer to string
# print(type(num)) # <class 'str'>
# #Conversion of string to float
# #String to float conversion happens only when string contains a valid float value and not any other characters. Otherwise, it will raise a ValueError.  
# weight = "70.5"
# print(type(weight)) # <class 'str'>
# weight = float(weight) # converting string to float
# print(type(weight)) # <class 'float'>

#Average of two numbers
marks1 = float(input("Enter marks of first subject: "))
marks2 = float(input("Enter marks of second subject: "))
average = (marks1 + marks2) / 2
print("The average of the two subjects is: ", average)
