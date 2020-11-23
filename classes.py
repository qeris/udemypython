class Employee:
    # numOfEmp = 0
    raiseAmount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        # Employee.numOfEmp += 1

    def fullName(self):
        return "{} {}".format(self.first, self.last)

    def applyRaise(self):
        self.pay = int(self.pay*self.raiseAmount)

    @classmethod
    def setRaiseAmount(cls, amount):
        cls.raiseAmount = amount

    @classmethod # alternative constructor
    def from_string(cls, empStr):
        first, last, pay = empStr.split(",")
        return cls(first,last,pay)

    @staticmethod
    def isWorkDay(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
# print(Employee.numOfEmp)

emp1 = Employee("Ethan", "Schoultz", 26000)
# emp1.first = "Ethan"
# emp1.last = "Schoultz"
# emp1.email = "mail@mail.com"
# emp1.pay = 26000

emp2 = Employee("Test", "User", 50000)
# emp2.first = "Test"
# emp2.last = "user"
# emp2.email = "test@user.com"
# emp2.pay = 500
# print(emp1.fullName())

# emp1.fullName()  # These two lines are the same
# Employee.fullName(emp1)  # These two lines are the same

# print(emp1.__dict__)
# print(Employee.__dict__)
# print(emp1.pay)
# emp1.applyRaise()
# print(emp1.pay)
# print(Employee.numOfEmp)
# print(Employee.raiseAmount)
# Employee.setRaiseAmount(1.04)
# print(emp1.raiseAmount)
# print(emp2.raiseAmount)

# empStr1 = "John,Doe,10000"
# empStr2 = "Jane,Smith,12000"
# empStr3 = "Paul,Blart,5000"
# newEmp = Employee.from_string(empStr1)
# print(newEmp.first)
# print(newEmp.pay)

# import datetime
# myDate = datetime.date(2016,7,11)
# print(Employee.isWorkDay(myDate))

class Developer(Employee):
    raiseAmount = 1.10

    def __init__(self, first, last, pay, progLang):
        super().__init__(first, last, pay)
        self.progLang = progLang

dev1 = Developer("Dev", "One", 11000, "Java")
dev2 = Developer("Dev", "Two", 14000, "Python")

# print(dev1.email)
# print(dev2.email)
# print(dev1.email)
# print(dev1.progLang)

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def addEmp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remEmp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def printEmp(self):
        for emp in self.employees:
            print("-->", emp.fullName())

mgr1 = Manager("Man","One",90000,[dev1])
# print(mgr1.email)
# mgr1.addEmp(dev2)
# mgr1.printEmp()
# mgr1.remEmp(dev1)
# mgr1.printEmp()

# print(isinstance(mgr1, Employee))
# print(issubclass(Manager, Developer))