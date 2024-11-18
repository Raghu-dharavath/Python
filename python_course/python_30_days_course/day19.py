########## Python Lambda ###########

# A lambda function is a small anonymous function

# syntax : 
# lambda arguments : expression

var = lambda a:a+10

print(var(20))


mult = lambda b,c,d : b*c*d
print(mult(2,3,4))


def mult(a,b,c):
    return a*b*c

print(mult(2,3,4))


def myfunc(n):
    return lambda a,b:a+b*n

mult = myfunc(4)
print(mult(5,2))

# mult = lambda a:a*4
# print(mult(5))


def myfunc(n):
    return lambda a:a*n

double = myfunc(2)
triple = myfunc(3)

print(double(4))
print(triple(4))


########### Arrays ################

# creating an array containing car names

cars = ["Ford", "volvo", "bmw"]
print(cars)
print(type(cars))

x = cars[0]
print(x)

cars[0] = "Honda"

print(len(cars))

for x in cars:
    print(x)

cars.append("benz")
cars.remove()


