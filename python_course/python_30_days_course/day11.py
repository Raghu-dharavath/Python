# for list

my_list = [3,4,5,6,7]
for x in my_list:
    if x%2==0:
        print(x)


### list comprehension ########

my_list = [3,4,5,6,7,8,9,11]

my_list1 = [print(x**2) for x in my_list]
my_list1 = [x**2 for x in my_list] 
print(my_list1)

my_list = ['apple','banana','kiwi']

# for x in my_list:
#     print(x.upper())

mylist = [x.upper() for x in my_list]
print(mylist)

fruits = ['apple','banana','kiwi',2,3,4,5,6]

new_list = [x if x!='banana' else "orange" for x in fruits] 

print(new_list)


nums = [x if x%2==0 else "odd" for x in range(10) ]  # [0,1,2]
print(nums)

## join two lists
list1 = ['a','b','c']
list2 = [1,2,3]

# print(list1+list2)

for x in list2:
    list1.append(x)

print(list1)








