import random
def ng():
  ntg=random.randint(1,100)
  guess=None
  print("Welcome to the Number Guessing Game!")
  print("I have selected a number between 1 and 100. Can you guess what it is?")
  while guess!=ntg:
    guess = int(input("Enter your guess: "))
    if guess < ntg:
      print("Too low! Try again.")
    elif guess > ntg:
      print("Too high! Try again.")
    else:
      print("Congratulations! You guessed the number.")

ng()
