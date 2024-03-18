#Task 1: Random Choice Game



import random


list = ['Board game', 'fishing pole', 'catchers mitt']


while True:
    guess = input("Guessing game: ")
    if guess == random.choice(list):
        print(guess)
        break
    