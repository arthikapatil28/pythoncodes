from abc import ABC,abstractmethod
class TouchScreenLaptop(ABC):
    def __init__(self,name,version):
        self.name=name
        self.version=version
    @abstractmethod
    def scroll(self):
        pass
    @abstractmethod
    def click(self):
        pass
    
class Hp(TouchScreenLaptop):
    def __init__(self,name,version,id):
        super().__init__(name,version)
        self.id=id
    def scroll(self):
        print("scrolled Down")
    @abstractmethod
    def click(self):
        pass
class Dell(TouchScreenLaptop):
    def __init__(self,name,version,ssn):
        super().__init__(name,version)
        self.ssn=ssn
    def scroll(self):
        print("scrolled Up")
    @abstractmethod
    def click(self):
        pass
class HpNotebook(Hp):
    def __init__(self,name,version,id,ssn):
        Hp.__init__(self,name,version,id)
        self.ssn=ssn
    def scroll(self):
        print("Scrolled")
    def click(self):
        print("Clicked button on HP")
class DellNotebook(Dell):
    def __init__(self,name,version,ssn,id):
        Dell.__init__(self,name,version,ssn)
        self.id=id
    def scroll(self):
        print("Scrolled")
    def click(self):
        print("Clicked button on Dell")
laptop = HpNotebook("HP", "John", 10, 200)
print(laptop.name)
print(laptop.version)
print(laptop.id)
print(laptop.ssn)
laptop.click()
laptop.scroll()


laptop = DellNotebook("Dell", "Kohn", 20, 300)
print(laptop.name)
print(laptop.version)
print(laptop.id)
print(laptop.ssn)
laptop.click()
laptop.scroll()
