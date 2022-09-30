# define a class employee with instance object variables empid , name , salary write  __int__() method in the class to initilize
# instance object variables .also define instance methods to input fields and display field values

class Employee:
    def __init__(self):
        self.empid=None
        self.name=None
        self.salary=None

    def show(self):
        empid=input("Enter the employee id:-")
        name=input("Enter the employee name:-")
        salary=int(input("Enter the salary of the employee:-"))

e=Employee()
e.show()
