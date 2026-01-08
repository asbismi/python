class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Employee(person):
    def __init__(self, name, age, employee_id):
        person.__init__(self, name, age)  # call person constructor directly
        self.employee_id = employee_id
    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}")


class parttime(person):
    def __init__(self, name, age, working_hours):
        person.__init__(self, name, age)  # call person constructor directly
        self.working_hours = working_hours
    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Working Hours: {self.working_hours}")


class consultant(Employee, parttime):
    def __init__(self, name, age, employee_id, working_hours, project_name):
        person.__init__(self, name, age)  # call person constructor once
        self.employee_id = employee_id
        self.working_hours = working_hours
        self.project_name = project_name
    def show_details(self):
        print(
            f"Name: {self.name}, Age: {self.age}, "
            f"Employee ID: {self.employee_id}, "
            f"Working Hours: {self.working_hours}, "
            f"Project Name: {self.project_name}"
        )


# Objects
p1 = person("Anil", 30)
e1 = Employee("Beena", 35, "EMP101")
pt1 = parttime("Charan", 25, 20.5)
c1 = consultant("Deepa", 40, "CONS202", 15.0, "AI Development")

# Display
p1.show_details()
e1.show_details()
pt1.show_details()
c1.show_details()
