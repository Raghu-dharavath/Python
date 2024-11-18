##### interview questions #######

#### 1.swaping ######
# exchange the values 
""" 
def swaping(a,b):
    a,b=b,a
    return a,b
a=10
b=20
print(f"before swapping: a= {a}, b= {b}")
a,b = swaping(a,b)
print(f"after swapping: a= {a}, b= {b}")
 """
### 2.factorial #####

# 0! = 1
# 4! = 4*3*2*1 = 24
# 5! = 5*4*3*2*1 = 120
""" 
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

n=4
result = factorial(n)
print(f"the factorial of {n} is : {result}") """



#### Ascending  list ##########
""" 
mylist = [5,6,2,3,7,4]

# mylist.sort()
mylist.sort(reverse=True)
print(mylist) """

###### even numbers #######
# n=10 => even : 0,2,4,6,8,10,12,14,16,18
#         odd : 1,3,.....

""" n=20
print("even : ")
for i in range(0,n):
    if i%2==0:
        print(i,end=" ")
print()
print("odd : ")
for i in range(0,n):
    if i%2!=0:
        print(i,end=" ") """




