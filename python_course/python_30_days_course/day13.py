######### Unpacking a tuple ######

# fruits = ('apple','banana','kiwi','grapes', 'pinapple','guva','mango')

# (white,*green, yellow, red) = fruits

# print(white)
# print(green)
# print(yellow)
# print(red)

###### loop tuples ######

colors = ('red','white','blue','orange','green',"black")


for x in colors:
    if 'r' in x:
        print(x)
    else:
        print("there is no r charecter")
    



colors = ('red','white','blue','orange','green',"black")


for x in range(0,len(colors)):
    if 'r' in colors[x]:
        print(x)
    else:
        print("there is no r charecter")
    





