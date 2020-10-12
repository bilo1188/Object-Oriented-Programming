class Employee:

    increment =  2

    def __init__ (self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def increase(self):
        self.salary = int(self.salary * self.increment)

    @classmethod

    def change_increment(cls,amount):
        
        cls.increment = amount
    @classmethod

    def from_str(cls,emp_string):
        fname,lname,salary = emp_string.split("-")
        return cls(fname,lname,salary)
    @staticmethod

    def isopen(day):
        if day=='sunday':
            return False
        else:
            return True

    def __add__(self,salary):
        return self.salary + self.salary

    def __repr__(self):
        return 'Employee({},{},{})'.format(self.fname,self.lname,self.salary)
    def __str__(self):
        return 'the name of emplyee is {}'.format(self.fname)

Bilal = Employee('bilal','bro',19000)

print(repr(Bilal))
print(str(Bilal))

#Altaf = Employee('altaf','bro',18000)
#print(Bilal+Altaf)
#print(Bilal.experience)
#print(bilal.salary )       
#Employee.change_increment(5)
#bilal.increase()
#print(bilal.salary )        
#xyz = Employee.from_str("quaid-azam-1000")
#print(xyz.salary)
#bilal = Employee('bilal','prof',10000)        
#print(Employee.isopen('sunday'))
