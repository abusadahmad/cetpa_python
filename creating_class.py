class employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = employee('Corey','scafer',50000)
emp_2 = employee('John','smith',6500)

print(emp_1.email)
print(emp_2.email)

print(emp_1.full_name())

