############## Python Inheritance #############

# Parent class
# Child class


##### parent class ######

class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname,self.lname)

x = Person("Virat","Kohli")
x.printname()

##### child class ######

class Student(Person):
    pass

s = Student("Rohit","sharma")
s.printname()


################### super() Function #####################



##### parent class ######

class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname,self.lname)

##### child class ######

class Student(Person):
    def __init__(self,year,fname,lname):
        super().__init__(fname,lname)
        self.year = year
    def dept(self):
        print(self.year)

s = Student(2020,"Virat","Kohli")
s.printname()
s.dept()

########## Python Iterators #################
## Iterator vs Iterable

mytuple = ("apple","banana","cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))

for x in mytuple:
    print(x)


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <=20:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
    
myobject = MyNumbers()
myiter = iter(myobject)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

for x in myiter:
    print(x)

# i=1
# while i<10:
#     print(next(myiter))
#     i+=1


