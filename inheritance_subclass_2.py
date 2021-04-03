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

class developer(employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lng):
        super().__init__(first, last, pay)
        self.prog_lng = prog_lng

class manager(employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employess = []
        else:
            self.employess = employee

    def add_emp(self, emp):
        if emp is not in self.employess:
            self.employess.append(emp)

    def rremove_emp(self, emp):
        if emp is self.employess:
            self.employess.remove(eemp)

    def print_emp(self):
        for emp in self.employess:
            print('--->' , emp.fullname())

dev_1 = developer('Corey','scafer',50000,'python')
dev_2 = developer('John','smith',6500,'java')


mgr_1 = manager('sui','smith',900000, [dev_1])
print(mgr_1.email)

mgr_1.print_emp()