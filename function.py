#Function is a block of code which only runs when it is called. We can pass data, known as parameters, into a function. A function can return data as a result.
#Function is defined using def keyword followed by function name and parentheses ().
# def add(a:int, b:int):
#     #code block
#     added = a + b
#     return added

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# result = add(num1, num2)
# print(result)

#Example function for **kwargs
def example_function(*args, **kwargs):
    print("Positional arguments: ", args)
    print("Keyword arguments: ", kwargs)    

example_function(1, 2, 3, name="John", age=30)
example_function(1, "banana", "cherry", fruit1="apple", fruit2="banana")
example_function(1, 2, 3, 4, 5, name="John", age=30, city="New York", country="USA")

#Example function for **kwargs
def example_function(**kwargs):
    print("Keyword arguments: ", kwargs)

example_function(name="John", age=30)
