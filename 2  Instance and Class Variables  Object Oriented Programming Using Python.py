class Employee:

    increment =  2

    def __init__ (self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def increase(self):
        self.salary = int(self.salary * self.increment)
        
bilal = Employee('bilal','prof',10000)
print(bilal.salary )
bilal.increase()
print(bilal.salary )
        
