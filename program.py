from student import *

class Program(Student):
    def __init__(self, program):
        self.program=program
        self.student=[]

        
    def addStudent(self,name):
        self.student.append(name)

    def sumOfFee(self):
        total=0
        for student in self.student:
            total += student.getFee()
        return total

