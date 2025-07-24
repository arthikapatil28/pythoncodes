from abc import abstractmethod,ABC
class BMW(ABC):
    def __init__(self,name,id,make):
        self.name=name
        self.id=id
        self.make=make
    @abstractmethod
    def drive(self):
        pass
class Threeseries(BMW):
    def __init__(self,name,id,make,cruise):
        BMW. __init__(self,name,id,make)
        self.cruise=cruise
    def drive(self):
        print("Threeseries is been driven")
class Fiveseries(BMW):
    def __init__(self,name,id,make,parking):
        BMW. __init__(self,name,id,make)
        self.parking=parking
    def drive(self):
        print("Threeseries is been driven")
bmw = Threeseries("Car", 12, "2018", True)
print(bmw.make)
print(bmw.name)
print(bmw.id)
print(bmw.cruise)
bmw.drive()

bmw=Fiveseries(False,"Bus",10,"2019")
print(bmw.make)
print(bmw.name)
print(bmw.id)
print(bmw.parking)
bmw.drive()
    
