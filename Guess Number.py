from random import randint

easy_level_turns = 10
hard_level_turns = 5

def check_answer(guess, answer, turns):
  """checks answer against guess, returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

def set_difficulty():
  level = input("Choose a difficult. Type 'easy' or 'hard': ")
  if level == "easy":
    return easy_level_turns
  else:
    return hard_level_turns

def game():
  print("Welcome to the guessing game!")
  print("I'm thinking of a number between 1 and 100")
  
  answer = randint(1, 100)
  
  turns = set_difficulty()
  
  guess = 0
  
  while guess != answer:
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)
    print(f"You have {turns} attempts remaining to guess the number.")
    if turns == 0:
      print("You've ran out of guesses, you lose!")
      return
    elif guess != answer:
      print("Guess again!")
game()