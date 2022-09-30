#write the program to create 3 user objects and find the youngest of all

class user:
    def __init__(self,age):
        self.age=age
first=user(21)
a=first.age
second=user(22)
b=second.age
third=user(23)
c=third.age
if a>b and a>c:
    print("youngest is",a)
elif b>a and b>c:
    print("youngest is",b)
else:
    print("youngest is",c)
