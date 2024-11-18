####### Remove Dictionary items #####

# pop()

thisdict={"name":"Anilet","class":1,"school":"jmhs"}
# hie.pop("class")

print(thisdict["class"])

# popitem()

# thisdict.popitem()

# del thisdict["name"]
# print(thisdict)

# del thisdict

print(thisdict)

thisdict.clear()

print(thisdict) # {}



### Looping ###
thisdict={"name":"Anilet","class":1,"school":"jmhs"}
for x in thisdict:
    print(x)

for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)

for x in thisdict.keys():
    print(x)


for x,y in thisdict.items():
    print(x,y)


###### copy Dictionaries ########

# copy()

mydict = {"location":"india"}
person = {'name':"varun","age":20,"city":"hyd"}

mydict = person.copy()

print(mydict)


mydict = dict(person)
print(mydict)


###### Nested Dictionaries ######

myfamily = {
                "child1":{"name":"Virat","year":2021},
                "child2":{"name":"Virat","year":2021},
                "child3":{"name":"Rohit","year":2022}
            }

# child1={"name":"Virat","year":2021}
# child2={"name":"Virat","year":2021}
# child3={"name":"Rohit","year":2022}

# myfamily = {"child1":child1, "child2":child2, "child3":child3}

print(myfamily["child2"]["year"])

###### looping nested dictionary #######

for x,y in myfamily.items():
    print(x)
    for a,b in y.items():
        print(a,b)




######## data types #########

"""

1.Integer datatypes(int,float,complex)
2.Sequence dataypes(list,tuple,range,string)
3.mapping dataypes(dictionary)
4.set datatypes(set, frozen-set)
5.Boolean dataypes(True,False)
6.None dataypes(None)

"""

