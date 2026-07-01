#if statement executes a block of code if the condition is true. If the condition is false, it skips the block of code.
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

# marks = int(input("Enter your marks: "))
# if marks >= 90:
#     print("You got A grade.")
# elif marks >= 80:
#     print("You got B grade.")
# elif marks >= 70:
#     print("You got C grade.")
# else:

# total_amount = int(input("Enter the total amount: "))
# if total_amount >= 5000:
#     discount = total_amount * 0.1
#     print(f"You got a discount of {discount}.")
# elif total_amount >= 3000:
#     discount = total_amount * 0.05
#     print(f"You got a discount of {discount}.")
# elif total_amount >= 1000:
#     discount = total_amount * 0.02
#     print(f"You got a discount of {discount}.")
# else:
#     print("You are not eligible for any discount.")

#match statement is used to match a value against a series of patterns and execute a block of code based on the first matching pattern. It is similar to switch statement in other programming languages.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter the operation (+,-,*,/): ")
# match operation:
#     case "+":
#         print(f"The sum of {num1} and {num2} is: ", num1 + num2)
#     case "-":
#         print(f"The difference of {num1} and {num2} is: ", num1 - num2)
#     case "*":
#         print(f"The product of {num1} and {num2} is: ", num1 * num2)
#     case "/":
#         if num2 != 0:
#             print(f"The division of {num1} and {num2} is: ", num1 / num2)
#         else:
#             print("Division by zero is not allowed.")   
#     case _:
#         print("Invalid operation.")
if operation == "+":
    print(f"The sum of {num1} and {num2} is: ", num1 + num2)    
elif operation == "-":
    print(f"The difference of {num1} and {num2} is: ", num1 - num2)
elif operation == "*":
    print(f"The product of {num1} and {num2} is: ", num1 * num2)
elif operation == "/":
    if num2 != 0:
        print(f"The division of {num1} and {num2} is: ", num1 / num2)
    else:
        print("Division by zero is not allowed.")
else:
    print("Invalid operation.")