import random
import sys

def main():
    human = input("Chose p for paper, s for scissor, r for rock, or e to Exit :")
    gesture = {
        'p': 'Paper',
        's': 'Scissors',
        'r': 'Rock',
        'e': 'Exit'
    }
    # computer = gesture.get(random.choice(['p', 's', 'r']))
    computer = gesture.get(random.choice('psr'))
    if human == 'e':
        sys.exit("You pressed e for Exit, bye!")
    elif human == 'p' and computer == 'Paper':
        print(" You both chose Paper. Draw")
    elif human == 's' and computer == 'scissors':
        print("You both chose scissors. Draw")
    elif human == 'r' and computer == 'rock':
        print("You both chose rock. Draw")
    elif human == "r" and computer == "Paper":
        print("Rock loses to paper. You Lose!")
    elif human == "r" and computer == "Scissors":
        print("Rock beats scissors. You Win!")
    elif human == "p" and computer == "Scissors":
        print("Paper loses to scissors. You Lose!")
    elif human == "p" and computer == "Rock":
        print("Paper beats rock. You Win!")
    elif human == "s" and computer == "Rock":
        print("Scissors loses to rock You Lose!")
    elif human == "s" and computer == "Paper":
        print("Scissors loses to paper. You Win!")
    else:
        print("Roh oh that was not p, r, s, or e, please try again")
        main()

    restart = input("Would you like to play again?: ")
    if restart == "yes" or restart == "y":
        main()
    if restart == "n" or restart == "no":
        print ("Script terminating. Goodbye.")



main()