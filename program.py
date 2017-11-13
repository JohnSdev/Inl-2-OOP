from student import *

class Program(Student):
    def __init__(self, program):
        self._program=program
        self._student=[]

        
    def addStudent(self,name):
        self._student.append(name)

    def sumOfFee(self):
        total=0
        for student in self._student:
            total += student.getFee()
        return total

