print("Welcome to Quiz Game.")
answer = input("Do you want to play? ")
if answer.lower()!='yes':
    quit()
print("Let's Go!!!")
score = 0

answer = input("Q1 : what is CPU stands for ? ")
if answer.lower()=="control processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("Q1 : what is RAM stands for ? ")
if answer.lower()=="random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("Q1 : what is DOM stands for ? ")
if answer.lower()=="document object model":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("Q1 : what is GUI stands for ? ")
if answer.lower()=="graphical user interface":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("Q1 : what is ROM stands for ? ")
if answer.lower()=="read only memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


print(f"Your Score is {score} out of 5 !!!")
print("You got "+str((score/5)*100)+"%")