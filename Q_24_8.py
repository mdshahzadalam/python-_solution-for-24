#  wrt 7th questions create 3 laptop objects and add them to the list in the sorted order based on the ram size
class laptop:
    def __init__(self,brand,ram,cpu,hdd):
        self.brand=brand
        self.ram=ram
        self.cpu=cpu
        self.hdd=hdd

    def showconfig(self):
        print(self.brand,self.ram,self.cpu,self.hdd)

first=laptop("DELL",8,"INTELL","1TB")

second=laptop("MACBOOK",16,"POS","1SSD")

third=laptop("HP",12,"HIGH","512 SSD")

if first.ram>second.ram and first.ram>third.ram:
    first.showconfig()
elif second.ram>first.ram and second.ram>third.ram:
    second.showconfig()
else:
    third.showconfig()







