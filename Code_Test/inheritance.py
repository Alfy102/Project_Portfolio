class Employee:
    raise_amaount=1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amaount)
        
class Developer(Employee):
    raise_amaount = 1.1
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang
        
class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first,last,pay)
        if employees is None:
           self.employees = []
        else:
           self.employees = employees       
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self,emp):
        if emp not in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
            print('--->',emp.fullname())
        



      
dev_1 = Developer('Corey', 'Shafer', 800, 'Python')
dev_2 = Developer('Silver', 'Bullet', 700, 'Java')
# print(dev_1.fullname())

mgr_1 = Manager('Sure', 'Smith', 9000, [dev_1])
print(mgr_1.email)
mgr_1.add_emp(dev_2)
# mgr_1.print_emps()


print(isinstance(mgr_1, Employee))
print(isinstance(dev_1, Employee))


print(issubclass(Manager, Employee))
# print(dev_1.email)
# print(dev_1.prog_lang)