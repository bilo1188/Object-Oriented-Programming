class Employee:

    increment =  2

    def __init__ (self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

        

    def increase(self):
        self.salary = int(self.salary * self.increment)
    @property
    def email(self):
        if self.fname == None:
            return 'email not fount'
        else:
            
            return self.fname+'.'+self.lname + '@gmail.com'

    @email.setter
    def email(self,given_email):
        name_list = given_email.split('@')[0].split('.')
        self.fname = name_list[0]
        self.lname = name_list[1]
        
    

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
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

if __name__ == '__main__':
    Bilal = Employee('bilal','bro',19000)
    Ali = Employee('ali','bhai',15000)
    print(Bilal.email,Ali.email)
    Bilal.lname = 'siddiqui'
    print(Bilal.email)
    Bilal.email = 'siddiqui.bilal@gmail.com'
    print(Bilal.email)

    del Bilal.email
    print(Bilal.email)

#print(repr(Bilal))
#print(str(Bilal))
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
