####### dict interview questions ########

# 1.create an empty dictionary

my_dict = {}

# 2.create a dict with key-value pairs

my_dict = {'name':"Ram","age":30,'city':"hyd"}

# Iterate through the keys in dict

for key in my_dict:
    print(key)

# Iterate through the values in dict

for value in my_dict.values():
    print(value)

# for both key,values

for key1,value in my_dict.items():
    print(key1,value)

# merge two dict

my_dict1 = {'name':"Ram","age":30,'city':"hyd"}
my_dict2 = {'school':"chaitanya","marks":300}

new_dict = {**my_dict1, **my_dict2}

print(new_dict)

# sort the dict by it's keys

my_dict = {'name':"Ram","age":30,'city':"hyd", "aarmy":True}

new_dict = sorted(my_dict.items())

print(dict(new_dict))

# update values in dict using another dict

my_dict = {'name':"Ram","age":30,'city':"hyd", "aarmy":True}
my_dict2 = {'school':"chaitanya","marks":300}

my_dict.update(my_dict2)

print(my_dict)


# dict comprehension
# {1:1,2:8,3:27,4:64,5:125}

n=5
my_dict = {}
for i in range(1,n+1):
    my_dict[i]=i**3

print(my_dict)

my_dict = {key:key**2 for key in range(1,n+1)}
print(my_dict)


########## sets questions #########
# empty set 
my_set = set()

# remove duplicates
lst = [1,2,2,3,4,4,5,5]

print(set(lst))

# find the length of sets

my_set = {2,3,4,5,6,7}
print(len(my_set))

# adding a num to a set 

my_set = {2,3,4,5,6,7}
my_set.add(9)

print(my_set)

# set union

set1 = {1,2,3,4,5}
set2 = {3,4,5}

union_set = set1.union(set2)
print(union_set)

intersection_set = set1.intersection(set2)
print(intersection_set)

# max,min
my_set = {2,3,4,5,6,7}

maximum = max(my_set)
minimum = min(my_set)

print(maximum,minimum)

