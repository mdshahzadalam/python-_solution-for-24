#write the program to delete the age property of the user

class user:
    def __init__(self):
        self.name="shahzad"
        self.age=23

s=user()
del(s.name)
#print(s.name)
print(s.age)