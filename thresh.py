import random

thresh_quotes = [
    "So many souls to liberate",
    "Hah! You're not worthy yet!",
    "Your spirit clings to hope. Pathetic.",
    "Beg harder, maybe I'll consider it.",
    "The mist is hungry tonight."
]

correct_phrase = "Lantern"
attempts = 0

while True:
    user_input =  input("Thresh: What do you say to receive my lantern, mortal?\n> ")
    attempts += 1

    if user_input.strip().lower() == correct_phrase.lower():
        print(f"Thresh: Very well... *a lantern glows in the mist* (You made it in {attempts} tries)")
        break
    else:
        print(f"Thresh: {random.choice(thresh_quotes)}")

#python woods.py