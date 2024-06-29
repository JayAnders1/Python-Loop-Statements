#Question 2 task 1

import random

moods = ["Happy", "Sad", "Energetic", "Calm", "Anxious", "Stressed", "Tired"]
selected_day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
time_of_day = ["morning", "afternoon", "evening"]

for day in selected_day:
    for time in time_of_day:
        mood = random.choice(moods)
        print(f"On {day} {time}, I was feeling {mood}.")
        