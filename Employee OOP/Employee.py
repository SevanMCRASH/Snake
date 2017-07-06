
class Employee():
    list = []
    list2 = []
    Mydict = dict()
    def __init__(self,salary):
        self.salary = salary
        self.addSalary(salary)

    def addSalary(self,salary):
        Employee.list.append(salary)

    def send(self,data):
        for i in Employee.list:
            if i == data:
                Employee.list2.append(i)

    def getMax(self):
        max = Employee.list[0]
        for i in Employee.list:
            if max < i:
                max = i
        return max

    def getMin(self):
        min = Employee.list[0]
        for i in Employee.list:
            if min > i:
                min = i
        return min

    def getAvarage(self):
        avarage = 0
        count = 0
        for i in Employee.list:
            avarage += int(i)
            count += 1
        avarage = avarage/count
        return avarage

    def getDepMax(self):
        max = Employee.list2[0]
        for i in Employee.list2:
            if max < i:
                max = i
        return max

    def getDepMin(self):
        min = Employee.list2[0]
        for i in Employee.list2:
            if min > i:
                min = i
        return min

    def getDepAvarage(self):
        avarage = 0
        count = 0
        for i in Employee.list2:
            avarage += int(i)
            count += 1
        avarage = avarage / count
        Employee.list2.clear()
        return avarage


