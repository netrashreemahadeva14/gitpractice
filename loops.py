#Loops allows to do repetitive tasks without writing the same code again and again. 
# There are two types of loops in Python: for loop and while loop.
#For loop is used to iterate over a sequence (list, tuple, string) or other iterable objects. It executes a block of code for each item in the sequence.
# for i in range(5): # range() function returns a sequence of numbers from 0 to 4. It is used to generate a sequence of numbers.
# for i in range(7, 71, 7): # range() function returns a sequence of numbers from 7 to 70. It is used to generate a sequence of numbers.
#     print(i) # prints the value of i in each iteration. 
#While loop is used to execute a block of code as long as the condition is true. It is used when we don't know the number of iterations in advance.
# i = 0 
# while i < 5:
#     print(i) # prints the value of i in each iteration.
#     i += 1 # increments the value of i by 1 in each iteration. It is used to avoid infinite loop.
#Password validation using while loop
# password ="python123"
# user = ""
# while user != password:
#     user = input("Enter the password: ")
#     if user == password:
#         print("Password is correct.")
#     else:
#         print("Password is incorrect. Try again.")

#ATM Pin validation using while loop
# pin = "1234"
# user_pin = ""
# while user_pin != pin: #If will check condition and exits, While will keep checking the condition until it is false.    
#     user_pin = input("Enter your ATM pin: ")
#     if user_pin == pin:
#         print("Pin is correct.")
#     else:
#         print("Pin is incorrect. Try again.")

#Nested loops are used when we want to execute a block of code inside another block of code. It is used when we want to iterate over a sequence of sequences.
# for i in range(1, 6): # outer loop
#     for j in range(1, 6): # inner loop
#         print(i, j) # prints the value of i and j in each iteration.  

for i in range(4): # outer loop
    for j in range(4): # inner loop
        print("*", end=" ") # prints the value of * in each iteration. end=" " is used to print the value of * in the same line.
    print() # prints a new line after each iteration of outer loop.