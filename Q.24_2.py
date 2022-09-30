# write a python program to create a user class with a method to greet the user

class user:
    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email
    def show(self):
        print(self.name,self.age,self.email)

s=user("Shahzad",23,"abc@gmail.com")
s.show()