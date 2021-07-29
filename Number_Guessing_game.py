""" Number Guessing Game Project(1)
----------------------------------------
"""
import random
def guessing_game():
    random_number = int(random.randint(1,20))
    print("Hello Buddy! Welcome to the game of guesses!")
    player_name = input("What's your name? ")
    wanna_play = input("Hi, {}, would you like to play the guessing game? (Enter Yes/No) ".format(player_name))
    attempts=0
    while wanna_play.lower() == "yes":
        try:
            guess = input("please Pick a number between 1 and 20 ")
            if 20<int(guess) or int(guess)<1:
                raise ValueError("Please guess a number within the given range")
            if int(guess) == random_number:
                print("Nice! You got it!")
                attempts += 1
                print("You took,{},attemts to guess a number! HA HA!".format(attempts))
                play_again= input("Would you like to play again? (Enter Yes/No) ")
                attempts = 0
                random_number = int(random.randint(1,20))
                if play_again.lower() == "no":
                    print("That's cool, have a good day!")
                    break
            elif int(guess) > random_number:
                print("your number is higher then Guessing Number")
                attempts += 1
            elif int(guess) < random_number:
                print("Your number is lower then Guessing Number")
                attempts += 1
        except ValueError as err:
            print("Oh no!, that's not a valid value.please Try again and Choose a Number Between Given Range...")
            print("Its look like Value Error Thats Why You got previous message")
            play__again=input("Would you like to play again? (Enter Yes/No)")
                
    else:
        print("That sounds cool, have a good day!")
if __name__ == '__main__':
    guessing_game()
