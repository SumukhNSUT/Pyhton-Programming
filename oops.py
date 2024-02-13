class Employee:
    company = "Google"  # class attribute
    salary = 30000  # class attribute
# class attributes are common for all members of class
# when we write rahul = Employee() , then it gets all properties in class atrributes
# stuff referring to single employee is instantaneous attributes

# In object-oriented programming (OOP), a class is a blueprint for creating objects (instances)
# It defines the properties (attributes) and behaviors (methods) that all objects of that type will have


harry = Employee()
rajni = Employee()

rajni.adress = "Adress 1"  # this is instantaneous attribute
# referring only rajni
# nothing to do with other employees

print(harry.company)
print(rajni.company)

# Modifying class variable using class name
Employee.company = "YouTube"

print(harry.company)
print(rajni.company)
print(harry.salary)
print(rajni.salary)

Employee.salary = 50000  # here rajni and harry both 50,000
print(harry.salary)
rajni.salary = 60000  # here rajni updated , harry at 50,000
# this is an instance attribute
print(rajni.salary)

sumukh = Employee()
print(sumukh.salary)
# salary was updated for all employees
# new salary for all employees is 50,000
print(sumukh.company)  # company of all employees were made youtube
