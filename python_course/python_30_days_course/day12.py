##### python tuples #####
# lst = [3,4,"hello",5,6.4848,5,5,8]
# print(lst)
# print(type(lst))

# sequence data types : list, tuple, range
# tuple is immutable (not changable)
# tuple can be represented by ()
# typle is ordered 

my_tuple = (3,4,5,6,7,8,9)
print(my_tuple)
print(type(my_tuple))

fruits = ("apple","banana","kiwi","kiwi")

print(fruits[0:3])
print(len(fruits))

name = ("apple",)
print(name)
print(type(name))

tuple2 = (list, False, True, False)
print(tuple2)

# tuple() constructor
my_tuple = tuple(("apple","banana","kiwi","kiwi"))
print(my_tuple)

# python collections(Arrays)
# 4-collection data types => list, tuple, set, dict

### Python-Access Tuple items 

fruits = ("apple","banana","kiwi","kiwi","grapes")

print(fruits[0:5])

# negetive indexing

print(fruits[-1])
print(fruits[-4:])


print('grapes' in fruits )


#### Update Tuples ####

x = ("rohit",'virat','pandya')
y = list(x)

print(y) # ["rohit",'virat','pandya']

y.append('bumrah')

print(y)

z = tuple(y)
print(z)

my_list =  ["rohit",'virat','pandya']

for item in my_list:
    # item = "tohit"
    if 'a' in item:
        print(item)
        

