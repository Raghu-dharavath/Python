########## Interview Questions ##########

# 1.find the number of times that the substring accures in the given string?

string = "ABCDCDCABABAB"
substring = "AB"
count = 0

for i in range(0,len(string)):
    my_string = string[i:len(string)]
    if my_string.startswith(substring):
        count+=1
print(count)

# 2.string compression [input_string = "aabbbcdd", output_string="a2b3cd2"]

string = "aabbbcdd"
current_ele = string[0]
count=1
lst = [] # ['a','2','b','3','c','1','d','1']

for i in range(1,len(string)):
    if current_ele==string[i]: # d==d
        count+=1
    else:
        lst.append(current_ele)
        if count>1:
            lst.append(str(count))
        current_ele=string[i]
        count=1

lst.append(current_ele)
if count>1:
    lst.append(str(count))


compressed_string = "".join(lst)
print(compressed_string)


# 3.find common letters between two strings

str1 = "charan"
str2 = "chandra"

output = "chanr"

str1 = set(str1)
str2 = set(str2)

common_letters = str1 & str2
result = "".join(common_letters)
print(result)

# count the number of vowels in string

string = "hellohi"
vowels = "aeiouAEIOU"
count=0

for item in string:
    if item in vowels:
        count+=1

print(count)


# find longest word in a string

string = "hi Hello How are you I am from Hyderabad , I am vijayanagaram learing python"
longest = ""

my_string = string.split()

for item in my_string:
    if len(item)>len(longest): 
        longest=item 

print(longest)


# find most frequent word in a string

string = "hi how how how how hi how are hi you"
new_string = string.split()

frequency = {}

for item in new_string:
    if item in frequency:
        frequency[item]+=1
    else:
        frequency[item]=1

longest = 0
string = ""
for key,value in frequency.items():
    if value>longest:
        longest=value
        string = key
print([string,longest])
    







