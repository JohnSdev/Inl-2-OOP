
from person import Person

class Staff(Person):
    def __init__(self, name, address, school, pay):
        

        self._school=school
        self._pay=float(pay)
        return super().__init__(name, address)
    def getSchool(self):
        return self._school
        
    def setSchool(self, school):
        self._school=school

    def getPay(self):
        return self._pay

    def setPay(self, pay):
        self._pay=float(pay)

    def __str__(self):
        return "Staff[{0},school={1},pay={2:.2f}]".format(super().__str__(), self.getSchool(), self.getPay())
    