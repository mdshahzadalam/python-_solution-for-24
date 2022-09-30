#write a python program to create 2 objects of the usre class and assign different values

class user:
    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email
    def show(self):
        print(self.name,self.age,self.email)

first=user("Shahzad",23,"abc@gmail.com")
first.show()
second=user("MySirG",45,"saurabhshukla@gmail.com")
second.show()