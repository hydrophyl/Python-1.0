import datetime

my_date = datetime.date(1996, 10, 6)

class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls,amount): #cls: class variable names
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Corey','Schafer',50000)
emp_2 = Employee('David','User',100000)

Employee.set_raise_amt(1.05)

#NOTE create new employees
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Jbean-Dove-60000'
emp_str_3 = 'Jaha-Dope-80000'

new_emp_1 = Employee.from_string(emp_str_1)

print(Employee.num_of_emps)
print(Employee.is_workday(my_date))