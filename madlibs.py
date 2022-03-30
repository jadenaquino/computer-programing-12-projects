story_choice = input("Which story would you like to play? 1, 2 , 3, q: ")


noun = input("noun: ")
adj = input("adjective: ")
plural_noun = input("plural_noun: ")
verbing = input("verbing: ")
place = input("place: ")
number = input("number: ")
body = input("body: ")


def madlib_1():
    print(f"In the world of {place} where the {plural_noun} have fallen! \
the hero is {verbing} at the face of the monster. The battle that happened in a {noun} which took {number} \
days! As the hero chases the {adj} monster, the hero was able to defeat the monster by going for it's {body} \
avenging those who fallen.")




def madlib_2():
    print(f"a man was going to the {place} in the evening and suddenly {plural_noun} appeared \
out of nowhere, {verbing} the man who was just passing by. The man runs away and heads very far \
and arrives in a {noun}. The man enters it and wanders around it, {number} minutes later the man is {adj} \
frightened by the missing {body} piece of a skeleton that had dropped and soon the man ran as fast as he can.")



def madlib_3():
    print(f"In the land of {place} where all your wishs are granted and desired. You will have to seek the {noun} that grants those wishs, \
it is said in order to get those wishs you will need to pass the {plural_noun} to get there. Once you have arrived you will need to find a \
{body} in order to start the wish process, when the wish process has ended it is said the one who grants wishs is a {adj} being. It will \
will ask you for {number} wishs and you will have to say your wishs, once you answer you will be {verbing} as your wish is being granted. \
You will then be transported back to where you came from and enjoy these wishs.")



while story_choice != "q":
    if story_choice == "1":
        madlib_1()
        story_choice = input("Which story would you like to play? 1, 2 , 3, q: ")
    elif story_choice == "2":
        madlib_2()
        story_choice = input("Which story would you like to play? 1, 2 , 3, q: ")
    elif story_choice == "3":
        madlib_3()
        story_choice = input("Which story would you like to play? 1, 2 , 3, q: ")
    else:
        print("You must pick a valid option!")
        story_choice = input("Which story would you like to play? 1, 2 , 3, q: ")
print("thanks for playing the game!")



















