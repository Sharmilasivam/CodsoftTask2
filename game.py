import random

def play_game():
    choices = ['stone', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    user_choice = input("Choose stone, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        play_game()

    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'stone' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'stone') or (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")

    play_again = input("Do you want to continue playing? (yes/no): ").lower()
    if play_again == 'yes':
        play_game()
    else:
        print("Thanks for playing!")

play_game()
