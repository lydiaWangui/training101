# a class is a blueprint/prototype i.e. a collection of related properties and methods


class Student:
    # class variables are variables that are shared across all instances
    regNumber = ""
    grade = ""
    total = 0
    average = 0

    def __init__(self,math, eng,kis,sci,ssr):
        self.totalMarks(math, eng,kis,sci,ssr)
        self.calcAvg(self.total)

    # a function inside aclass is called a method
    def totalMarks(self, math,eng,kis,sci,ssr):
        self.total = math+eng+kis+sci+ssr

    def getGrade(self):
        self.grade = "This grade is affected"
    def calcAvg(self,tot):
        # always put self before what you are calculating
        self.average= tot/5
#
# variable james is an object of a class method
# an object is an instance of a class

james = Student(23,45,78,98,89)
lydia = Student(78,89,67,50,89)

amran = Student(56,32,21,45,32)

print(james.total)
print(lydia.total)
print(amran.total)

print(james.average)
print(lydia.average)

james.getGrade()
print(james.grade)

