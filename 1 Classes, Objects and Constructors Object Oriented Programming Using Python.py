class Employee:


    def __init__ (self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        
bilal = Employee('bilal','prof',10000)

print(bilal.fname , bilal.salary )
        
