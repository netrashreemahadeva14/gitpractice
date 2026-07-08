#exception is an error that occurs during the execution of a program. It is an event that disrupts the normal flow of the program's instructions. In Python, exceptions are raised when errors occur at runtime. When an exception is raised, the normal flow of the program is interrupted, and Python looks for a special block of code called an exception handler to handle the error.
# try block is used to wrap the code that may raise an exception. If an exception occurs in the try block, the code in the except block is executed. If no exception occurs, the code in the except block is skipped.
# except block is used to handle the exception that occurs in the try block. It contains the code that is executed when an exception occurs. If no exception occurs, the code in the except block is skipped.

# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))
# print("The division of two numbers is: ", number1 / number2) # This line may raise a ZeroDivisionError if number2 is 0.
try:
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))
        print("The division of two numbers is: ", number1 / number2) # This line may raise a ZeroDivisionError if number2 is 0. 
except ZeroDivisionError:
        print("Division by zero is not allowed. Please enter a non-zero number.")