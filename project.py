import random
import art
import emoji
from termcolor import colored

def main():
    ascii_art = art.text2art("Rock, paper, scissors!")
    print(colored(ascii_art, 'blue'))
    cscore = 0
    pscore = 0
    md = int(input("Press 1 for tournament mode and 2 for endless mode "))

    while md!=1 and md!=2:
        print("Please enter 1 or 2")
        md = int(input("Press 1 for tournament mode and 2 for endless mode "))

    if md == 1:
        print("Rock: 1".ljust(15) + "Paper: 2".ljust(15) + "Scissor: 3")
        rounds = int(input("Enter the number of rounds you would want to play "))
        for _ in range(rounds):
            playert = int(input("Rock, paper, or scissors? "))

            while playert < 1 or playert > 3:
                print("Please enter a number between 1 and 3 ")
                playert = int(input("Rock, paper, or scissors? "))

            comp = random.randint(1,3)
            print(f"Your choice: {playert}")
            print(f"Computer's choice: {comp}")

            if playert == comp:
                output = emoji.emojize("It's a Draw! :slightly_smiling_face: \n")
                print(colored(output, 'yellow'))
                pscore += 1
                cscore += 1
            elif (playert == 1 and comp == 3) or (playert == 2 and comp == 1) or (playert == 3 and comp == 2):
                output = emoji.emojize("You win! :trophy: \n")
                print(colored(output, 'green'))
                pscore += 1
            else:
                output = emoji.emojize("Computer wins! :laptop:\n")
                print(colored(output, 'red'))
                cscore += 1

        if pscore>cscore:
            ascii_art2 = art.text2art("You Won!")
            print(colored(ascii_art2, 'green'))
            print(f"Your score: {pscore}\nComputer's score: {cscore}")
            ascii_art3 = art.text2art("Thank You For Playing!")
            print(colored(ascii_art3, 'magenta'))

        elif cscore>pscore:
            ascii_art2 = art.text2art("You Lost!")
            print(colored(ascii_art2, 'red'))
            print(f"Your score: {pscore}\nComputer's score: {cscore}")
            ascii_art3 = art.text2art("Thank You For Playing!")
            print(colored(ascii_art3, 'magenta'))

        else:
            ascii_art2 = art.text2art("It's a Draw!")
            print(colored(ascii_art2, 'yellow'))
            print(f"Your score: {pscore}\nComputer's score: {cscore}")
            ascii_art3 = art.text2art("Thank You For Playing!")
            print(colored(ascii_art3, 'magenta'))

    else:
        print("Rock: 1".ljust(15) + "Paper: 2".ljust(15) + "Scissor: 3".ljust(15) + "End Game: 4")
        playere = 0

        while playere!=4:
            playere = int(input("Rock, paper, or scissors?"))

            while playere<1 or playere>4:
                print("Please enter a number between 1 and 4")
                playere = int(input("Rock, paper, or scissors?"))

            if playere == 4:
                break
            comp = random.randint(1,3)
            if playere == comp:
                output = emoji.emojize("It's a Draw! :slightly_smiling_face:\n")
                print(colored(output, 'yellow'))
            elif (playere == 1 and comp == 3) or (playere == 2 and comp == 1) or (playere == 3 and comp == 2):
                output = emoji.emojize("You win! :trophy: \n")
                print(colored(output, 'green'))
            else:
                output = emoji.emojize("Computer wins! :laptop:\n")
                print(colored(output, 'red'))

        ascii_art3 = art.text2art("Thank You For Playing!")
        print(colored(ascii_art3, 'magenta'))


def player_tournament_input(playert):
    if not isinstance(playert, int):
        raise ValueError("Input must be an integer")
    return playert in [1, 2, 3]

def player_endless_input(playere):
    if not isinstance(playere, int):
        raise ValueError("Input must be an integer")
    return playere in [1, 2, 3, 4]

def rounds_input(rounds):
    if not isinstance(rounds, int):
        raise ValueError("Input must be an integer")
    return rounds > 0

def computer_input(comp):
    if not isinstance(comp, int):
        raise ValueError("Input must be an integer")
    return comp in [1, 2, 3]

if __name__ == "__main__":
    main()
