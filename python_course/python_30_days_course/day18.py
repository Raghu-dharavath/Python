############ Functions ###########

""" 
# syntax :
def function_name():
    #statements
    return num

function_name() """

def my_function():
    print("Hello from a function")


my_function()


def my_function(fname,lastname):
    print(fname + " and " + lastname)

my_function("virat","kohli")
my_function("Rohit","sharma")
my_function("Rishab","Pant")

####### Arbitrary Arguments ########


def my_function(*players):
    print("the top players is :"+players[2])

my_function("Rohit","virat","bumrah","tom","Pant")

###### Keyword Arguments ############

def my_function(child2,child3,child1):
    print("the youngest child is "+child3)

my_function(child1="bob",child2="ramu",child3="hari")


###### Arbitrary Keyword Arguments #########

def my_function(**child):
    print("the older child is "+child['child3'])

my_function(child1 = "Varun",child2="rahul",child3="ramesh",child4="jithesh")

######### Default Parameter value ########

def my_function(country = "india"):
    print("I am from "+country)

my_function("USA")
my_function("swedan")
my_function()


###### Passing a List as an Argument ######

def fruits_fun(food):
    for x in food:
        print(x)


fruits = ["apple","banana","cherry"]
numbers = [1,2,3,4,5,6]
fruits_fun(fruits)
fruits_fun(numbers)

######### Return values #########


def my_fun(x):
    multiplication = 5*x
    return multiplication

result = my_fun(5)

print(result)

print(my_fun(6))

####### positional-only Arguments 

def my_function(num):
    for x in num:
        if x%2==0:
            print("even",x)
        else:
            print("odd",x)


numbers = [1,2,3,4,5,6]
my_num = [44,5,67,889,97655]
my_function(numbers)
my_function(my_num)


######### Recursion Functions #######

# 5! = 5*4*3*2*1 = 120



def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

num = int(input("enter a number : "))
result = factorial(num)
print(f"factorial of {num} is", result)



