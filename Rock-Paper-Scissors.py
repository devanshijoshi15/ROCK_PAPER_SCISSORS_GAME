import random

def play_game():
  # Choices available
  choices = ["rock", "paper", "scissors"]

  # User input
  user_choice = input("Choose rock, paper, or scissors: ").lower()
  while user_choice not in choices:
    user_choice = input("Invalid choice. Please choose rock, paper, or scissors: ").lower()

  # Computer's random choice
  computer_choice = random.choice(choices)

  # Determine the winner
  if user_choice == computer_choice:
    result = "It's a tie!"
  elif user_choice == "rock" and computer_choice == "scissors":
    result = "You win! Rock beats scissors."
  elif user_choice == "paper" and computer_choice == "rock":
    result = "You win! Paper covers rock."
  elif user_choice == "scissors" and computer_choice == "paper":
    result = "You win! Scissors cut paper."
  else:
    result = "You lose. "

  # Display the result
  print(f"\nYou chose: {user_choice.capitalize()}")
  print(f"Computer chose: {computer_choice.capitalize()}")
  print(result)

  # Ask to play again
  play_again = input("\nDo you want to play again? (y/n): ").lower()
  if play_again == "y":
    play_game()

# Start the game
play_game()
