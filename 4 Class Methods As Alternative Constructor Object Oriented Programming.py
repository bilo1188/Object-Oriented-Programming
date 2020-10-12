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
        
#bilal = Employee('bilal','prof',10000)

#print(bilal.salary )

        
#Employee.change_increment(5)
#bilal.increase()
#print(bilal.salary )
        
xyz = Employee.from_str("quaid-azam-1000")

print(xyz.salary)

