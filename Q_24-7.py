#write a program to create a laptop class with 4 attributes (brand , ram, cpu,hdd) and 2 methods (showconfig()
#to print the values , __init__() to initiallize the values)
class laptop:
    def __init__(self,brand,ram,cpu,hdd):
        self.brand=brand
        self.ram=ram
        self.cpu=cpu
        self.hdd=hdd

    def showconfig(self):
        print(self.brand,self.ram,self.cpu,self.hdd)

s=laptop("DELL",8,"INTELL","1TB")
s.showconfig()




