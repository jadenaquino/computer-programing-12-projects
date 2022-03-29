import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}'))
        if guess < random_number:
            print('incorrect, try again, number is hot')
        elif guess > random_number:
            print('incorrect, try again, number is cold')

    print(f'good job, you have guessed the number {random_number} correctly')




def gamemode1():
    print("i guess the number!")
    guess(100)


def gamemode2():
    print("let the computer guess the number!")
    guess(50)

def gamemode3():
    print("i want to quit!")


gamemode = input("what whould you like to play? (gamemode1, gamemode2, gamemode3):")

if gamemode == "gamemode1":
    gamemode1()
elif gamemode == "gamemode2":
    gamemode2()
elif gamemode == "gamemode3":
    gamemode3()
else:
    print("you musy pick a valid option")







def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'r':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??' ). lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        
    print(f'Yes! the computer guessed your number,{guess}, correctly!')

guess(50)





