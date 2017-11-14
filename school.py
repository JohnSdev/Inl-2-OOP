from staff import Staff
from program import Program


class School(Staff):
    def __init__(self, school):
        self._school=school
        self._program=[]
        self._staff=[]

    def addStaff(self, staffname): 
        self._staff.append(staffname)

    
    def addProgram(self, programName):
        self._program.append(programName)

    def sumOfPay(self):
        total=0
        for pay in self._staff:
            total += pay._pay
        return total

    def getProfit(self, sumPay, sumFee):
        if sumFee > sumPay:
            return True
        return False 



