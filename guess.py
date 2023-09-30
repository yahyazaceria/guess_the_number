import random

number = random.randint(0, 100)
guessed = int(input("Guess a number between 1 and 100: "))

while guessed != number:
  if guessed > number:
    guessed = int(input("Lower: "))
  elif guessed < number:
    guessed = int(input("Higher: "))

if guessed == number:
    print("You have guessed the number!") 
 