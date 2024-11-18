# data structures 

# integer : int,float,complex
# sequence : string,list,tuple and range
# set : set and frozenset
# mapping : dictionary
# boolean : True or False
# None : None

########### list ################

# list is a collection of storing different datatypes
# list is mutable(changable)
# []
# ordered
# list is sequence datatype
""" 
lst = ["apple","banana","grapes"]
lst.append("pinapple")

lst = [3,4,5,6,7,8,9]
print(lst[1:5])
lst = [True,False,False]

print(lst[-1])
print(type(lst))

# list() constuctor

my_list = list(("apple","banana"))
print(my_list)
 """
#check if item exists

lst = [3,4,5,6,7,8,9]

print(66 not in lst)

if 6 in lst:
    print("it is there in list numbers")
else:
    print("it is not there")

# change list items
lst = [3,4,5,6,7,8,9]
lst[1] = "apple"
print(lst)

lst[1:4] = ['apple','banana','kiwi']

print(lst)
print(len(lst))


lst = [3,4,5,6,7,8,9]
lst.append("apple")
print(lst)

lst.insert(2,"kiwi")
print(lst)





