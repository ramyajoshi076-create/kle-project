class Employee:
    def __init__(self, name, salary, experience, age):
        self.name = name
        self.salary = salary
        self.experience = experience
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Experience:", self.experience)
        print("Age:", self.age)

s1 = Employee("SHRIRAM", 99000, "02 years", 19)
s1 = Employee("JOEL", 90000, "09 years", 25)
s1.display()