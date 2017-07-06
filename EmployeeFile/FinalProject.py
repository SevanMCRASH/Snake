#SEVAN MARDIROSSIAN
import os
import pickle
import json
def main():
    if (os.path.exists('employee.dat')):
        mydict = Load('employee.dat')
    else:
        mydict = {}
    Flag = True
    while Flag == True:
        employee = mydict
        print(" 1.Add an Employee\n", "2.Find an Employee\n", "3.Display Statistics\n", "4.Delete an Employee\n",
            "5.Findan Employee by"
            " ID\n", "6.Display All Employees\n", "7.Exit")
        while True:
            try:
                choice = int(input("Please make choice of an integer as your choice"))
                break
            except ValueError:
                    print("Oops!  That was no valid number.  Try again...")

        if(choice == 1):
            AddanEmployee(employee)

        if (choice == 2):
            FindanEmployee(employee)

        if (choice == 3):
            DisplayStatistics(employee)

        if (choice == 4):
            DeleteAnEmployee(employee)

        if (choice == 5):
            FindanEmployeeID(employee)

        if (choice == 6):
            DisplayAllEmployees(employee)

        if (choice == 7):
            Save(employee, 'employee.dat')
            Load('employee.dat')
            Flag = Exit()

        if (choice > 7):
            print("Oops!  That was no valid number.  Try again...")
            Flag = True

def AddanEmployee(employee):
    name = input("Please enter the name employee:")
    name = name.lower()
    while(name in employee):
        name = input("Please make a different choice")
        name = name.lower()
    employeeID = input("Please enter the ID of the employee:")
    department = input("Please enter the Department of the employee:")
    title = input("Please enter the Title of the employee:")
    salary = input("Please enter the Salary of the employee:")

    tmpemp = dict()
    tmpemp['ID'] = employeeID.lower()
    tmpemp['Dept'] = department.lower()
    tmpemp['Title'] = title.lower()
    tmpemp['Salary'] = salary.lower()

    employee[name] = tmpemp

def FindanEmployee(employee):
    key = input("OK, Please enter the Employees name:")
    key = key.lower()
    while (key not in employee):
        key = input("Please make a different choice")
        key = key.lower()
    for i in employee.keys():
        if i == key:
            print("Employee:")
            print("\tName: " + i)
            print("\tEID: " + employee[i]['ID'])
            print("\tDept: " + employee[i]['Dept'])
            print("\tTitle: " + employee[i]['Title'])
            print("\tSalary: " + employee[i]['Salary'])

def DisplayStatistics(employee):
    dep_dict = dict()
    for key in employee:
        if employee[key]['Dept'] in dep_dict:
            dep_dict[employee[key]['Dept']] += 1
        else:
            dep_dict[employee[key]['Dept']] = 1
    for j in dep_dict:
        print("Department",j,"has", dep_dict[j], "employees")

def DeleteAnEmployee(employee):
    empname = input("OK, Please enter the Employees name:")
    empname = empname.lower()
    while (empname not in employee):
        empname = input("Please make a different choice")
        empname = empname.lower()
    print("Employee has been deleted")
    del employee[empname]

def FindanEmployeeID(employee):
    EID = input("OK, Please enter the Employees ID:")
    EID = EID.lower()
    for i in employee:
        if(employee[i]['ID'] == EID):
            print("Employee:")
            print("\tName: " + i)
            print("\tEID: " + employee[i]['ID'])
            print("\tDept: " + employee[i]['Dept'])
            print("\tTitle: " + employee[i]['Title'])
            print("\tSalary: " + employee[i]['Salary'])
        else:
            print("ID dosen't exist")


def DisplayAllEmployees(employee):
    print("Displaying all Employees")
    for i in employee:
        print("Employee:")
        print("\tName: " + i)
        print("\tEID: " + employee[i]['ID'])
        print("\tDept: " + employee[i]['Dept'])
        print("\tTitle: " + employee[i]['Title'])
        print("\tSalary: " + employee[i]['Salary'])

def Exit():
    print("program terminated")
    return False

def Save(employee, filename):
    writefile = open(filename, 'wb')
    pickle.dump(employee, writefile)
    writefile.close()
    print("Progress saved")

def Load(filename):
    try:
        readfile = open(filename, 'rb')
        mydict = pickle.load(readfile)
        readfile.close()
        print(mydict)
    except EOFError:
        mydict = {}

    return mydict
main()