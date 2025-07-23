class Patient:
    def setid(self,id):
        self.__id=id
    def getid(self):
        return self.id
    def setname(self,name):
        self.__name=name
    def getname(self):
        return self.name
    def setssn(self,ssn):
        self.__ssn=ssn
    def getssn(self):
        return self.ssn
p=Patient()
p.setid(12)
p.setname("Arthika")
p.setssn(12301)
print(p._Patient__id)
print(p._Patient__name)
print(p._Patient__ssn)
