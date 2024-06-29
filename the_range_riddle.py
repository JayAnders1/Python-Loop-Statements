#Question 1 Task 1

import random

moods = ["Happy", "Sad", "Energetic", "Calm", "Anxious", "Stressed", "Angry"]
day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


for mood in range(7):
    mood_in_day = random.choice(moods)
    print(f"My mood on {day[mood]} is {mood_in_day}.")


