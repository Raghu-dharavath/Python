#### set constructor #########

set1 = {1,2,2,3,4,5}

#set()

thisset = set(("apple","banana","cherry"))
print(thisset)

for x in thisset:
    print(x)

print("banana" not in thisset)

thisset.add('orange')

print(thisset)

print(len(thisset))

set1 = {1,2,2,3,4,5}
set2 = {44,55,66}
set1.update(set2)

print(set1)

##### Remove set items ####
set1 = {1,2,2,3,4,5}
# set1.remove()

# set1.pop()

# set1.discard(10)

# set1.clear()

# del set1

print(set1)

####### python - join sets #######

set1 = {1,2,2,3,4,5}
set2 = {44,55,66,34,23,45}
set3 = {'apple','banana'}
set4 = {"john","Tom"}

set5 = set1.union(set2,set3,set4)
print(set5)

set5 = set1 | set2 | set3 | set4
print(set5)

#### join a set and a tuple #######

set3 = {'apple','banana','John'}
set4 = ("john","Tom","Tom")

set6 = set3.union(set4)
print(set6)


set3 = {'apple','banana','john'}
set4 = {"john","Tom","Tom"}

set6 = set3 & set4
print(set6)

set3 = {'apple','banana','john',1,True}
set4 = {"john","Tom","Tom",'apple'}

set3.intersection_update(set4)
print(set3)

set3 = {'apple','banana','john',1,True}
set4 = {"john","Tom","Tom",'apple'}

set6=set3-set4
print(set6)


