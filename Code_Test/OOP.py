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
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
emp_1 = Employee('Corey', 'Shafer', 9000)
emp_2 = Employee('Milo', 'Nesquick', 8000)
#---------------------------------------------------------------------------------------
emp_str_1 = 'John-Doe-9000'
emp_str_2 = 'Johnny-Silverhand-1000'
emp_str_3 = 'Johnny-Derp-6000'

new_emp_1 = Employee.from_string(emp_str_1) #send the hypened dash string to from_string @classmethod
new_emp_2 = Employee.from_string(emp_str_2) # in order to split it, the classmoethod from_string then
new_emp_3 = Employee.from_string(emp_str_3) # returns the first, last, and pay. This then gets send back to Employee class for normal process
#---------------------------------------------------------------------------------------
Employee.set_raise_amount(1.05)

print(new_emp_1.fullname)
print(new_emp_2.email)
print(new_emp_3.email)


# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)