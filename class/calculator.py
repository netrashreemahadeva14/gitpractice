class calculator:
    def add(self, a, b):
        print(a + b)

    def subtract(self, a, b):
        print(a - b)

    def multiply(self, a, b):
        print(a * b)

    def divide(self, a, b):
        if b != 0:
            print(a / b)
        else:
            print("Error: Division by zero")

    