#Tasks1: Your Mood Today
import random

moods = ["Happy", "Sad", "Energetic", "Calm"]
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for index in range(len(days_of_week)):
    print(f"My mood today is: + {random.choice(moods)}, on a {days_of_week[index]}")



