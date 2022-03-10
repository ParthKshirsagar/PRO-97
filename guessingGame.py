import random
number = random.randint(1,9)
chances = 5
print("Number Guessing Game")
print("Guess a number (between 1 and 9)")
while chances <= 5:
    while chances > 0:
        guess = int(input("Enter your guess:- "))
        if(guess == number):
            print("Congratulation YOU WON!!!")
            break
        elif(guess<number):
            chances -= 1
            if not chances == 0:
                print("Your guess was too low: Guess a number higher than", guess)
        else:
            chances -= 1
            if not chances == 0:
                print("Your guess was too high: Guess a number lower than", guess)
    break
if(chances == 0):  
    print("YOU LOSE!! The number was:", number)