##### Difference #######

set1 = {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}

set3 = set1.difference(set2)

print(set3)

#### difference_update() #####

set1 = {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}

set1.difference_update(set2)

print(set1)

######## symmetric differeces() or ^ #######

set1 = {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}

set3 = set1.symmetric_difference(set2)

print(set3)



####### symmetric_differece_update()  #######

set1 = {"apple","banana","cherry"}
set2 = {"apple","banana","cherry","orange"}

set1.symmetric_difference_update(set2)

print(set1)


print(set2.issuperset(set1))



########## Python Dictionaries ###########
# Dictionary is used to store data values in key:value pairs.
# Dictionary not allowed duplicates and changeable


set1 = {"apple","banana","cherry"}
my_dict = {"name":"Rahul","age":20,"company":"google","year":1998,"year":2020}
print(my_dict)

#### length ##
print(len(my_dict))

My_dict = {
                "name":"hari",
                "age":20,
                "year":2020,
                "salary":200000.00,
                "games":['cricket','hockey','chess'],
                "numbers":(2,3,4,5,6,7)
            }

print(My_dict)

print(type(My_dict))

###### dict() constructor #######

thisdict = dict(name="tom",age=20,country="india")
print(thisdict)


###### Python-Access Dictionary Items #######

My_dict = {
                "name":"hari",
                "age":20,
                "year":2020,
                "salary":200000.00,
                "games":['cricket','hockey','chess'],
                "numbers":(2,3,4,5,6,7)
            }

print(My_dict["games"])

print(My_dict.get("games"))

### accessing only keys() #####

print(My_dict.keys())


My_dict["fruits"]=["apple","banana","mango"]

print(My_dict)

print(My_dict.values())

#### get items() #####

print(My_dict.items())









