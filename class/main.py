#Class is a blueprint for creating objects in Python. It defines a set of attributes and methods that the objects of the class will have.
#object is an instance of a class. It is created using the class constructor and can access the attributes and methods defined in the class.
#self is a reference to the current instance of the class. It is used to access the attributes and methods of the class.
from calculator import calculator
from students import students
from employee import employee  

cal = calculator()
student1 = students("Harshil", 16, "10th")
employee1 = employee("John", 25, "Software Engineer")

cal.add(10, 5)
student1.display_info()
employee1.display_info()

