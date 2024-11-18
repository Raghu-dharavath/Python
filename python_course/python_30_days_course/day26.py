######## user input #######

# username = input(r"Enter\n username: ")
# print(username)


######### map, filter and Reduce #######

""" 
nums = [1,2,3,4,5,6]


multi = list(map(lambda n:n*3, nums))
print(multi)

odds = list(filter(lambda n:n%2!=0, multi))
print(odds)


from functools import reduce

sum = reduce(lambda a,b:a+b, nums)
print(sum)
 """
""" 
lst1 = [23,34,45,12,37,26,100]
lst2 = [14,23,100,45,26,74,56]
result = []

# o/p : [23,26,45]

for item in lst1:
    if item in lst2:
        result.append(item)

print(result) """

# question : print prime numbers from 1 to 100
# question2 : find a string is palindrome or not


######### Python File Open #######

#### create, read, update and delete


""" file = open(r"E:\my_folder\demo.txt","r" )


print(file.readline())
print(file.readline())
print(file.readline()) 
"""

# file = open(r"E:\my_folder\demo.txt","r" )

# for x in file:
#     print(x[0:10])

file = open(r"E:\my_folder\demo.txt","r" )

print(file.readline())

file.close()


##### python file append ########
f = open(r"demo2.txt", "a")

f.write("Now the file has more content!!!")

f.close()

###### python file write

f = open(r"demo2.txt", "w")

f.write("it was overwritten!!!")

f.close()


###### create new file

""" f = open(r"demo2.txt", "x")

f.write("it was overwritten!!!")

f.close()
 """

###### delete

import os

os.remove("demo2.txt")