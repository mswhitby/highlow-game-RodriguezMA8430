import random

lower_bound = 1
upper_bound = 100
max_attempts = 10

secret_number = random,randint(lower_bound, upper_bound)

def check_guess(guess, secret_number):
  if guess ==secret_number:
    return "Correct"
  elif guess > secret_number:
    return " Wrong! Too High
  else:
    return "Incorrect! Too Low"

def play_game():
  attempts = 0
  won = false

  while attemps < max_attempts:
    attempts += 1
    guess = get_guess()
    result = check_guess(guess, secret_number)

    if result == "Correct":
        print(f"Winner Winner Winner!")
        won = true
        break
    else:
        print(f"{result}. Try again!")

if not won:
    print(f"Sorry you ran out of tries. The number was {secret_number}."0

if __name__ == "__main__":
    print("Welcome to the Number Game!")
    play_game()

