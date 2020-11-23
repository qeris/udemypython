class Employee:
    # numOfEmp = 0
    raiseAmount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullName(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullName())
        
    def fullName(self):
        return "{} {}".format(self.first, self.last)

    def applyRaise(self):
        self.pay = int(self.pay*self.raiseAmount)

    @classmethod
    def setRaiseAmount(cls, amount):
        cls.raiseAmount = amount

    @classmethod
    def from_string(cls, empStr):
        first, last, pay = empStr.split(",")
        return cls(first, last, pay)

    @staticmethod
    def isWorkDay(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    raiseAmount = 1.10

    def __init__(self, first, last, pay, progLang):
        super().__init__(first, last, pay)
        self.progLang = progLang


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


emp1 = Employee("Ethan", "Schoultz", 26000)
emp2 = Employee("Test", "User", 50000)
dev1 = Developer("Dev", "One", 11000, "Java")
dev2 = Developer("Dev", "Two", 14000, "Python")
mgr1 = Manager("Man", "One", 90000, [dev1])

# print(emp1)
# print(repr(emp1))
# print(emp1+emp2)
print(len(emp1))