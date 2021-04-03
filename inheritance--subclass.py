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


dev_1 = developer('Corey','scafer',50000,'python')
dev_2 = developer('John','smith',6500,'java')

print(dev_1.email)
print(dev_1.prog_lng)

print(dev_1.pay)
dev_1.apply_raised()
print(dev_1.pay)
