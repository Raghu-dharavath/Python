######## python -- classes and Objects ########

""" class Myclass:
    x=5
    y=20
    z=30

# print(Myclass)

p1 = Myclass()
print(p1.x)
print(p1.y) """


class Person:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city
    
per = Person("Tom",20,"USA")
p1 = Person("Ram",23,"India")

print(per.name)
print(per.age)
print(p1.city)


############# __str__() Function #########

class Person:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city
    def __str__(self):
        return f"{self.name} ({self.age})"

    
per = Person("Tom",20,"USA")
print(per)

####### object Methods #############

class Person:
    def __init__(self,name,age,city,a,b):
        self.name = name
        self.age = age
        self.city = city
        self.a = a
        self.b = b
        
    
    def my_function(self):
        return self.a+self.b
    
    def company(self,emp):
        return self.city,self.my_function(),emp

    
per = Person("Tom",30,"USA",5,6)
per1 = Person("hari",23,"India",2,3)
per.age = 30
del per.age
del per1
print(per.my_function())
print(per.city)
# print(per1.my_function())
print(per.company(200))

### create a class named as Hospital,properties(h_name,patients,staff,no_doct,specilists), 3-function()

class Person:
    pass











