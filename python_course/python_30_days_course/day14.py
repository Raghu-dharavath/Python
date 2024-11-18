#### Python - Join Tuples ####

tuple1 = ("a","b","c")
tuple2 = (1,2,3)

tuple3 = tuple1 + tuple2

print(tuple3)

#### multiply tuples ####

txt1=("apple","sri","hi","apple","apple")
word = "hi"

print(txt1.index(word))


############# python - sets ############

# A set is a collection which is unordered, unchangeable, and unidexed

# Duplicates are not allowed

myset = {"apple","banana","cherry","guva","mango","pinapple","orange", "apple","apple"}

print(myset)

# True and 1 

thisset = {"apple","banana","cherry", True, 1, 2}

print(thisset)

# False and 0 

thisset = {"apple","banana","cherry", False, 0, 2}

print(thisset)

###### length

print(len(thisset))

#### set items - Data types

set4={"hi","sri","hi"}
set2={2,6,9}
set4.update(set2)
print(set4)

""" 
set3={True,False}
set1={"hi","apple","kiwi",2,8,True,False}
print(set1)

for x in set1:
    print(x)

print("cherry" in set1)

set1.add("cherry")
print(set1)

"""