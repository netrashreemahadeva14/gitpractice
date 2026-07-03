#Dictionary is a collection of key-value pairs. It is unordered, mutable, and indexed. In Python, dictionaries are defined using curly braces {}.
#Dictionaries are used to store data values like a map, which, unlike other Data Types that hold only a single value as an element, holds key:value pair. Key-value is provided in the dictionary to make it more optimized.
#Dictionaries are unordered, mutable, and indexed. In Python, dictionaries are defined using curly braces {}.
#Dictionaries are used to store data values like a map, which, unlike other Data Types that hold only a single value as an element, holds key:value pair. Key-value is provided in the dictionary to make it more optimized.

# student = {
#     "name": "John",
#     "age": 20,
#     "city": "New York"
# }
# for key, value in student.items(): #student.items() returns a view object that displays a list of a dictionary's key-value tuple pairs. The for loop iterates over each key-value pair in the dictionary.
#     print(key, ":", value) # prints the key and value of each item in the dictionary.

#Adding items to a dictionary
# student = {
#     "name": "John",
#     "age": 20,
#     "city": "New York"
# }
# student["gender"] = "male"
# print(student) # prints the dictionary after adding a new key-value pair.

#Check if a key exists in a dictionary
student = {
    "name": "Harshil",  
    "age": 16,
    "city": "Bengaluru"
}
key_to_check = input("Enter the key to check: ")
if key_to_check in student:
    print(f"{key_to_check} exists in the dictionary")
else:
    print(f"{key_to_check} does not exist in the dictionary")