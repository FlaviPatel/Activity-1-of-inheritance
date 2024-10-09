class Person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print("Name is", self.name, "and  my idnumber is", self.idnumber)

class Employee(Person):
    def __init__(self, name, idnumber, salary, position):
        Person.__init__( self, name, idnumber)
        self.salary = salary
        self.position = position

employee1 = Employee("Joe", 12908, 20000, "HR")
employee1.display()