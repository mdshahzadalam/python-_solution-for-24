#  write a python program to create a school class and 3 instance variabkes adn 1 class variabel
class School:
    name="Science Public School"
    def __init__(self,prin_name,standard,address):
        self.prin_name=prin_name
        self.standard=standard
        self.address=address

s=School("Rekha","NC-9","Kako")
print(School.name)
print(s.prin_name)
print(s.standard)
print(s.address)










