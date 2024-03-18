
import random
moods = ["Happy", "Sad", "Energetic", "Calm"]
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
time_of_day = ['morning', 'afternoon', 'evening']

for mood in days_of_week:
    for day in time_of_day:
       print(f"On this {mood} of {day} I feel like this: + {random.choice(moods)}") 





# #Task 2: Your Mood Tracker
# import random

# mood = ["Sad", "Energetic", "Joyful", "Excited"] 
# time_of_day = ["morning", "afternoon", "evening"]

# for index in range(len(mood)):
#     for index in range(len(time_of_day)):
#         print(f"My different moods in a {time_of_day[index]}  + {random.choice(mood)}")
        
        


