
import random

# Read the input file of 5-letter words.
file = open("words.txt", "r")
words = [word.strip() for word in file.readlines()]

# Set the answer word to be a random one!
answer = random.choice(words)

# Play the game!
guess = ""
attempts = 0

while guess != answer and attempts < 6:
  guess = input("Enter a 5 letter guess: ")
  attempts = attempts + 1

  index = 0
  while index < len(answer):
    letter = guess[index]
    if letter == answer[index]:
        color = '💚'
    elif letter in answer:
        color = '🚧'
    else:
        color = '🚨'

    print(f"{letter} - {color}")
    index = index + 1

# Tell the user if they won or lost!
if guess == answer and attempts <= 6:
  print("You Won! That took " + str(attempts) + " guess(es).")
else:
  print("You lost. The answer was " + answer + ".")
