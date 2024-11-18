print("welcome to quiz game!!!!!!!!")

answer = input("Do you want to play : ") 
score = 0


if answer.lower()!='yes':
    exit()


answer = input("Q1: what is RAM stands for ? ")
if answer.lower()=="random access memory":
    print("correct!!!")
    score +=1
else:
    print("Incorrect!!!")

answer = input("Q2: what is ROM stands for ? ")
if answer.lower()=="read only memory":
    print("correct!!!")
    score +=1
else:
    print("Incorrect!!!")

answer = input("Q3: what is GUI stands for ? ")
if answer.lower()=="graphical user interface":
    print("correct!!!")
    score +=1
else:
    print("Incorrect!!!")

answer = input("Q4: what is API stands for ? ")
if answer.lower()=="application programming interface":
    print("correct!!!")
    score +=1
else:
    print("Incorrect!!!")

answer = input("Q5: what is www stands for ? ")
if answer.lower()=="world wide web":
    print("correct!!!")
    score +=1
else:
    print("Incorrect!!!")

print(f"you have got score={score} out of 5")

