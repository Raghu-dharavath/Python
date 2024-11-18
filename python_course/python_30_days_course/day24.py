############ RegEx Module #########


import re
""" txt = "The rain in Spain"

x = re.search("^The.*Spain$", txt)

print(x) """

# RegEx Functions

# findall, search, split, sub

###### MetaCharacters #########
""" 
[ ] = "[a-m]"
\   = "\d" 
.   = "he..o"
^   = "^hello"
$   = "Spaino$"
*   = "he.*o"
+   = "he.+o"
?   = "he.?o"
{}  = "he.{3}o
|   = "falls|stays"
()  = "()"
 """

txt = "hello raino 56 in 90 Spaino"

# x = re.findall("[a-m]", txt)
# x = re.findall("\d", txt)
# x = re.findall("he....", txt)
# x = re.findall("^he", txt)
# x = re.findall("Spaino$", txt)
# x = re.findall("he.*o", txt)
# x = re.findall("A.+n", txt)
# x = re.findall("he.?o", txt)
# x = re.findall("he.{7}o", txt)
# x = re.findall("raino|spaino", txt)
x = re.findall("(raino)", txt)


########### Special Sequences \ #########

""" 
\A = "\AThe"
\b = "ino\b"
\B = "ino\B"
\d = "\d"
\D = "\D"
\s = "\s"
\S ="\S"
\w ="\w"
\W ="\W"
\Z = "\Z"
 """

txt = "The rain$$$o 56 in 90 Spaino"
# x = re.findall(r"ino\b", txt)
x = re.findall(r"Spaino\Z", txt)

####### Sets #########

""" 
[arn]
[a-n]
[^arn]
[0123]
[0-9]
[0-5][0-9]
[a-z][A-Z]
[a-zA-Z]
[+]

 """

txt = "hTe rain$$$o 5+6 in 90 05 Spaino"
x = re.findall(r"[+]", txt)
                   

print(x)

phone_num = "my name is ramu my mobile no. is 994948559 I am from from hyd and my father no. 9949698849"

x = re.findall(r"\d+", phone_num)
                   

print(x)