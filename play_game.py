# play_game.py

import random

def get_user_choice():
    return input("Enter your choice (rock/paper/scissors): ").lower()

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    print(f"You chose {user_choice}")
    print(f"Computer chose {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        print("You win!")
    else:
        print("Computer wins!")

if __name__ == "__main__":
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    determine_winner(user_choice, computer_choice)
