from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, emp_id):
        self.name = name
        self.id = emp_id

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hours_worked, hourly_rate):
        super().__init__(name, emp_id)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

class Freelancer(Employee):
    def __init__(self, name, emp_id, project_count, pay_per_project):
        super().__init__(name, emp_id)
        self.project_count = project_count
        self.pay_per_project = pay_per_project

    def calculate_salary(self):
        return self.project_count * self.pay_per_project


