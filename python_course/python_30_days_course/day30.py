############## Interview Questions ####################


######## find largest number from given list ########## 

lst = [3,12,15,6,8,2,9] # [2,3,6,8,9,12,15]

largerst = 0

for item in lst:
    if item>largerst:
        largerst=item
print(largerst)

######## or ##########

lst.sort()
print("largest by sorting",lst[-1])


####### find second largest number from given list ######

lst = [3,12,15,13,22,6,8,2,9]

max_num = max(lst[0],lst[1])
second_largest = min(lst[0],lst[1])

for i in range(2,len(lst)):
    if lst[i]>max_num: #18>7
        second_largest=max_num
        max_num=lst[i]
    else:
        if lst[i]>second_largest: #10>14
            second_largest=lst[i]
    
print(second_largest)


######## or ##########

lst.sort()
print("second largest number by sorting",lst[-2])


########## fibonacci ###########

# 0,1,1,2,3,5,8,13,21,34,55.....

a=0
b=1
n=100
while a<n:
    print(a) 
    a,b = b,a+b
    i+=1

######## "123abc56efg" #######
# o/p => ['abc','efg']

string = "123abc56efg"
my_string = ""
my_list = []

for i in range(0,len(string)):
    if string[i].isdigit():
        my_string += string[i] 
    else:
        if my_string:
            my_list.append(my_string)
        my_string = ""
print(my_list)

######## "123abc56efg" #######
# o/p => ['abc','efg']





