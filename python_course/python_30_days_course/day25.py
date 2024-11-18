""" ########### search() #######

import re

text = "The raian in Spain"
x = re.search("in",text)

print(x)

############# split() Function

text1 = '''

b: Asserts a word boundary, ensuring that we match whole numbers only.
[89]: Matches the first digit being either 8 or 9839393.
\d{9}: Matches exactly nine digits following the first digit (making a total of 10 digits).
\b: Asserts another word boundary to ensure the number doesn't continue with more digits.


'''
text = "The rain in Spain"
x = re.split("9839393",text1)

print(x[0])


print(text1.split("9839393")[0])


########### sub function ########

import re

text = "The raian in Spain"
x = re.sub("\s","9",text)

print(x)
 """


############# Python PIP ############
# pip is a package manager
# import pandas

# print(dir(pandas))


######### Python Try Except ########

# try block test a block of code for errors

# except block lets you handle the error

# else block lets you excute code when there is no error

# finally 


######## Excption Handling ##########

""" try:
    x=10
    print(x)
    if x:
        y=10
        print(y)
except NameError:
    print("Variable y is not defined")
except IndentationError:
    print("expected an intented block")
except:
    print("An Error accured")
else:
    print("Nothing went wrong") """

try:
    x=10
    print(x)
    if x:
        # y=10
        print(y)

except NameError:
    print("Variable y is not defined")   
except IndentationError:
    print("expected an intented block")

finally:
    print("the 'try except' is finished")

###### Raise an exception #########

# x = -1
# if x<0:
#     raise Exception("Sorry, no numbers below of Zero")

x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")








