import random

number = random.randint(1,50)
name = input("What is your name? ")
number_of_guesses = 0
print("Ok! "+ name + "! Guess a number between 1 and 50. You have 5 chances to guess!")

while number_of_guesses < 5:
  guess = int(input())
  number_of_guesses += 1
  if guess < number:
    print("That's too low!")
  if guess > number:
    print("That's too high!")
  if guess == number:
    break

if guess == number:
  print("Congrats! "+ name + "! You guessed the number in " + str(number_of_guesses) + " tries!")
else:
  print("The number was " + str(number) + "!")