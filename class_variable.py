class employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
    def full_name(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raised(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = employee('Corey','scafer',50000)
emp_2 = employee('John','smith',6500)

# print(employee.__dict__)
# print(emp_1.__dict__)
employee.raise_amount = 1.05 #  here we change the value of raise amount
emp_1.raise_amount =1.7     # here raise amount chage for only imp_1

print(employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

