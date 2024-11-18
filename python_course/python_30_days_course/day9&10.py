""" lst = ['apple',2,4,5,"kiwi"]
lst.append('hi')


lst.insert(2,"hari") #two arguments
# print(lst)

###### extend list #######

lst = [2,3,4,5,6]
lst1 = ('apple','banana','grapes')

lst.extend(lst1)

print(lst)

#### Remove specified item #####
lst = [2,3,4,4,5,6]

lst.remove(4)

print(lst)

### pop ####
lst = [2,3,4,4,5,6,'apple']

lst.pop(2) #index
lst.pop()

print(lst)

#### del ###

lst = [2,3,4,4,5,6,'apple']

del lst[2]
del lst

### clear ######

lst = [2,3,4,4,5,6,'apple']

lst.clear()
print(lst)

### reverse
lst = [2,3,4,4,5,6,'apple']
lst.reverse()

print(lst)


### sort
lst = [55,34,2,39,10,12]


lst.sort(reverse=True)

print(lst)

### copy()
lst3 = lst.copy()
print(lst3)


lst = [55,34,2,39,10,12,2,2,2,2,2]
print(lst.count(2))

string = ""
 """

### for loop in list #########

""" lst = ["hello, hi I am raghu",[33,34,35,36],4,5,6,7,8,9,"hi",4,5,10]

name = "hi"
# print(lst[0]+" "+"Tom")

# lst = [2,3,4]
# print(lst[1])

for x in range(0,len(lst)):
    if lst[x]==name:
        print(x) 

for x in lst:
    print(x)

"""


####### while loop in list #######
""" 
lst = [4,5,6,7,8]

i=0
while i<len(lst):
    print(lst[i])
    i = i+1 """







        









