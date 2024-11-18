############ Polymorphism ##########

""" 
x = "hello world"
print(len(x))

mytuple = (1,2,3)
print(len(mytuple))

thisdict = {'name':'varun','age':20}
print(len(thisdict))


class Car:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("moving in water!")

class Plane:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Fly!")

car1 = Car("Ford",2020)
boat1 = Boat("ship",2021)
plane1 = Plane("kf",2022)

# car1.move()
# boat1.move()
# plane1.move()

for x in (car1,boat1,plane1):
    x.move()


##### Inheritance class Plymorphism

print("------------------------------")

class Vehicle:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("It will move!")

class Car(Vehicle):
    pass
class Boat(Vehicle):
    def move(self):
        print("ship move")
class Plane(Vehicle):
    def move(self):
        print("Fly!")


car1 = Car("Ford",2020)
boat1 = Boat("ship",2021)
plane1 = Plane("kf",2022)


for x in(car1,boat1,plane1):
    print(x.brand)
    print(x.model)
    x.move()
 """

############  Python Scopes ###########
# Local Scope 

# def myfunc():
#     x=5
#     print(x)

# myfunc()


# function inside function

def myfunc():
    x=100
    def myinnerfunc():
        print(x)
    myinnerfunc()
    
myfunc()

# global Scope 

mylist = [2,34,4]

def myfunc():
    print(mylist)
myfunc()

print(mylist)

#### Naming variables 

x=300
def myfunc():
    x=200
    print(x)
myfunc()
print(x)

# global keyword
x=300
def myfunc():
    global x
    x = 50

myfunc()
print(x)

#### Nonlocal keyword


def myfuct1():
    x = "vijay"
    def myfunct2():
        nonlocal x
        x = "hello"
    myfunct2()
    return x

print(myfuct1())



    

