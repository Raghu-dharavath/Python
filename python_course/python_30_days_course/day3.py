##### Logical Operators #########
""" 
# and or not

# a)logical and

#  A    B    A and B
#  0    0     0
#  1    0     0
#  0    1     0
#  1    1     1

a = 45>12 and 56>23
print(a) # True

b = 45>12 and 56<23
print(b)

# b) logical or

#  A    B    A or B
#  0    0     0
#  1    0     1
#  0    1     1
#  1    1     1

a = 23<90 or 46>25
print(a)

# c) not

# A    notA 
# 1     0
# 0     1

a = not(1) 
print(a) """
""" 
####### membership operators ########## a)in  b)not in
names = ['ram','hari','varun']

print("rahul" not in names)

########### Identity operators ######### a) is b) is not

x = 5
# print(type(x))

print(type(x) is not float)

########## Bitwise operators #########

# 1) bitwise AND

# 1 => 0001 =>   16      8       4         2       1
#              10000   1000     0100     0010     0001
 
# 01000 = 8

# 3 =>  0011 => 0+0+2+1 => 3
# 7 =>  0111 => 0+4+2+1 => 7

#10&7

# 13 => 1101
# 9  => 1001
#    => 1001 => 9

print(10&7)
print(13&9)

# 2) bitwise OR
print(10|7)


# 13 => 1101
# 9  => 1001
#    => 1101 => 13

print(13|9)

# 3) bitwise XOR(^):

#  A    B    A ^ B
#  0    0     0
#  1    0     1
#  0    1     1
#  1    1     0

# 13 => 1101
# 9  => 1001
#    => 0100 => 4

print("13^9:",13^9)

#### compliment(~)

# A => -(A+1) 
# ~10 => -(10+1) => -
print(~112)
 """

####### taking input from keyboard ######

# a = int(input("Enter a value: ")) 

# print("value:",a)
# print(type(a))
# print(a+a)

### type casting

a = 10
b = float(a)
print(b)




