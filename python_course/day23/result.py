""" import adding

adding.greeting("Murali")

print(adding.person["name"]) """

#### Naming a Module #######

import mymodule as mod

print(mod.person['city'])

##### Bult-in Modules ####

import os

print(os.getcwd())

import platform

x = platform.system()
print(x)


#### import From Module

from mymodule import person

print(person.keys())

#### python Datetime ######

import datetime

x = datetime.datetime.now()
print(x)


######## python Math #######

x = min(4,5,6,7,44,33,56,45)
print(x)

x = max(4,5,6,7,44,33,56,45)
print(x)

x = abs(-7.34)
print(x)

x = pow(2,3)
print(x)


import math

x = math.sqrt(64)
print(x)

# ceil(),floor()


print(math.ceil(1.4))
print(math.floor(1.4))

print(math.pi)


########## python Json ###########
import json

x = '{"name":"Tom","age":20}'

y = json.loads(x)

print(y["name"])

### convert python to json

x = {"name":"Kohli","age":23}

y = json.dumps(x)

print(y)
print(type(y))

x = json.dumps(["apple","banana","mango"])
print(json.dumps(x))
print(type(x))
print(json.dumps(22))


bigdata = {
            "name":"tom",
            "age":30,
            "married":True,
            "children":("varun","arun","charan"),
            "cars":['Ford',"honda","tata"],
            "education":[
                {
                    "school":"sr",
                    "college":"iit"
                },
                {
                    "mba":True,
                    "job":True
                }
            ]

           }

print(json.dumps(bigdata))

print(json.dumps(bigdata, indent=10))
print(json.dumps(bigdata, indent=10, separators=(" "," ** ")))
print(json.dumps(bigdata, indent=10, sort_keys=True))



