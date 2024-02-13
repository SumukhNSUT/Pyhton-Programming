class Employee:
    company = "Google"

    def getSalary(self):
        print("Salary is 100k")


harry = Employee()
harry.getSalary()
# same as Employee.getSalary(harry)
