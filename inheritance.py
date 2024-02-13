class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")


class programmer(Employee):
    language = "python"

    def getLanguage(self):
        print(f"The language is {self.language}")


e = Employee()
e.showDetails()
f = programmer()
f.getLanguage()
print(f.company)
# prints company from base class as inherited class don't have any attribute named company
