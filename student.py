
from person import Person

class Student(Person):
    def __init__(self, name, address, program, year, fee):
        self._program=program
        self._year=year
        self._fee=fee

        return super().__init__(name, address)

    def getProgram(self):
        return self._program

    def setProgram(self, program):
        self._program=program

    def getYear(self):
        return self._year

    def setYear(self, year):
        self._year=year

    def getFee(self):
        return self._fee

    def setFee(self, fee):
        self._fee=float(fee)

    def __str__(self):
        return "Student[{0},program={1},year={2},fee={3:.2f}]".format(super().__str__(), self._program, self._year, self._fee)
