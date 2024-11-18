###### interview questions #######
### prime numbers : 2,3,5,7,11,13,17,19,.....100

n=100

prime_numbers = []

for i in range(1,n): # i=1,2,3,4,5,,,,,,19
    if i>1:
        for j in range(2,i): # j=2,3,4,5,6,,,,,,19
            if i%j==0: 
                break
        else:
            prime_numbers.append(i)


print(tuple(prime_numbers))   # (2,3,5,,,,,,,,)

#### check wheather a number is prime or not ##########

n=13

if n>1:
    for i in range(2,n): # 1,2,3,4,...9
        if n%i==0:
            print("the given number is not prime")
            break
    else:
        print("the given number is prime")


#### find frequency of each number in list ##########
   
my_list = [1,2,3,2,2,3,4,5,5,5,6,6,6,6,7]

# output => {1:1,2:3,3:2,4:1,5:3,6:4,7:1}

frequency = {}

for item in my_list:
    if item in frequency:
        frequency[item]+=1
    else:
        frequency[item]=1

print(frequency)


###### find common elements btw 2 lists ########

list1 = [1,2,3,4,5,6,7,8,9]
list2 = [11,22,3,4,51,6,17,38,9]
# output = [3,4,6,9]
result = []

for item in list1:
    if item in list2:
        result.append(item)

print(result)


###### Remove Duplicates from list #######

my_list = [1,2,3,3,3,4,5,6,6,6,5,5,5,7,8]

# output => [1,2,3,4,5,6,7,8]
result = []

for item in my_list:
    if item not in result:
        result.append(item)

print(result)

####### or ############
print(set(my_list))












