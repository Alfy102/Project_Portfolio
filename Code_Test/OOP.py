#Python OOP

class Employee:

    raise_amount = 1.04
    num_emps = 0
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.full_name = '{} {}'.format(first,last)
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_emps +=1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

emp_1 = Employee('Corey', 'Shafer', 9000)
emp_2 = Employee('Milo', 'Nesquick', 8000)


Employee.set_raise_amount(1.05)
print(Employee.raise_amount)