class employee:

    raise_amount = 1.04
    num_of_emp = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
    def full_name(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raised(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = employee('Corey','scafer',50000)
emp_2 = employee('John','smith',6500)

employee.set_raise_amount(1.9)


emp_str_1 = 'john-doe-70000'
emp_str_2 = 'steve-smith-30000'
emp_str_3 = 'jan-doe-90000'

new_emp_1 = employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)



# static method called here
import datetime
my_date = datetime.date(2016, 7, 10)

print(employee.is_workday(my_date))