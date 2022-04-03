player = "player"
opponent = "opponent"
player_score = 0
opponent_score = 0
user_choice = input("Would you like to play? Y or Q: ")



import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors, 'l' for lizard, 't' for spock: ")
    computer = random.choice (['r', 'p', 's', 'l', 't'])
   

    if user == computer:
        return 'it\'s a tie'


    if is_win(computer, user):
        return 'you won!'
    
    return 'you lost!'




def is_win(opponent, player):

    
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or \
    (player == 'p' and opponent == 'r') or (player == 'l' and opponent == 't') or \
    (player == 't' and opponent == 'p') or (player == 'r' and opponent == 'l') \
    or (player == 's' and opponent == 'l') or (player == 'p' and opponent == 't') \
    or (player == 'l' and opponent == 'p') or (player == 't' and opponent == 'r'):
        return True




while user_choice != "Q":
    if user_choice == "Y":
        print(play())
        user_choice = input("Would you like to play? Y or Q: ")
    elif user_choice == "Q":
        print(play())
        user_choice = input("Would you like to play? Y or Q: ")
    else:
        print("that is an invalid answer!")
        user_choice = input("Would you like to play? Y or Q: ")


player_score, opponent_score = (0, 0)
if player == opponent:
    print("It's a tie")
elif (player, opponent):
    print("You win")
    player_score += 1
elif (opponent, player):
    print("I win")
    opponent_score +=1
else:
    print("invalid option")

print("Final Scores")
print("player {} opponent {}".format(player_score, opponent_score))


print("Thanks for playing the game!")
    


        









    