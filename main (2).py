import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

# Function to play the game
def play_game():
    # Choices available for the game
    choices = ['rock', 'paper', 'scissors']
    
    # User input
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    
    # Check if the user's choice is valid
    if user_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        return

    # Computer's random selection
    computer_choice = random.choice(choices)
    print(f"Computer ch
