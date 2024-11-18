######### slicing strings ########

text = "python"
text+"tom"
print(text+"tom")

print(text)


length = len(text)
print(length)

print(text[0:10])

########## negetive indexing ###########

print(text[-5:-2])


########### python modify strings ########

text = "PYthaP" #PYTHON

print(text.upper())

print(text.lower())

print(text.strip())

print(text.replace("P","H"))

a = "hello, world, python, language"
b = a.split(",")
print(a.split(","))

print(b[1])

############ string Concatenation + #########
a = 'Hello'
b = 'World'
c = "python"
print(a+" "+b+" "+c)

word = "HELLO world python world world"

######## Format - strings #########
age = 24
txt = f"My name is John, I am {age*2}"
print(txt)

name = "tom"

name1 = "Hello, {}".format(name)
print(name1)



word = "HELLO world python world world"

print(word.islower())
print(word.isupper())

my_string = "iam24"

print(my_string)


######## python Booleans (True or False) ##########

print(10<9)

a = 100
b = 200

if b>a and a<b:
    print("b is greater than a")
else:
    print("b is not greater than a")

print(bool(0))

print(bool("abc"))
print(bool(123))
print(bool(['apple','grapes']))

print(bool(0))
print(bool(False))
print(bool(None))
print(bool(""))
print(bool([]))
print(bool(()))


################# list ##############






