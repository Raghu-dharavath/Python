import random

print("Welcome to Number Guessing Game!!!")
answer = input("Do you want to play?")
if answer.lower()!='yes':
    quit()

print("Let's Go!!!!")

random_num = random.randrange(1,100)
print(random_num)

print("You have total 5 Guessings")
count = 0

print("enter a number between 1 to 100 for guess!!!")

while True:
    answer = int(input("enter a number "))
    if answer<=100:
        if random_num//2>answer:
            print("Your number is very low, Guess again!!")
        elif random_num>answer:
            print("Your number is low, Guess again!!")
        elif random_num<answer//2:
            print("Your number is very high, Guess again!!")
        elif random_num<answer:
            print("Your number is high, Guess again!!")
        elif random_num==answer:
            print(f"Your Guess is correct!!!! you Got it in {count+1} Guesses")
            break
        count+=1
    else:
        print("Invalid input")

