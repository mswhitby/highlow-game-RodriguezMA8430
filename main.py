# main.py
import random

# define range and max_attempts
lower_bound = 1
upper_bound = 100
max_attempts = 10 

# generate the secret number
secret_number = random.randint(lower_bound, upper_bound)

# Get the user's guess
def get_guess():
  while True:
    try:
      guess = int(input(f"Guess a number between {lower_bound} and  {upper_bound}: "))
      if lower_bound <= guess <= upper_bound:
          return guess 
      else:
          print("Invalid number. Please enter valid number.")
          
# Validate guess
def check_guess(guess, secret_number):
    if guess == secret_number:
        return "Correct"
    elif guess < secret_number:
        return "Too low"
    else:
        return "Too high"
        
# track the number of attempts, detect if the game is over
def play_game():
    attempts = 0 
    won = False
    
  while attempts < max_attempts:
      attempts += 1 
     guess = get_guess()
     result = check_guess(guess, secret_number)
      
     if result == "Correct":
         print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts")
         won = True
         break
     else:
         print(f"{result}. Try again!")
         
  if not won:
      print(f"Sorry, you ran out of attempts! The secret number is {secret_number}.")
      
if__name__ == "__main__":
 print("Welcome to the number guessing game!")
 play_game()
