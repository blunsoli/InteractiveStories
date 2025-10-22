import time
print("You awaken in a world of blue static and upside down shadows.")
print("A voice echoes in your head, its Kakau's voice, distant but warm.\n")
time.sleep(2)

print("'To find me, you must solve what its hidden! Each answer opens a path, come to me, im scared :c'")
time.sleep(2)

score = 0
tries = 3

while tries > 0:
    riddle1 = input("\nA cube cries, a circle sings. I tick but i have no hands or face. What im I?\n>: ")
    if riddle1.strip().lower() == "clock":
        print("The cube stops crying. A stair appears.")
        score += 1
        break
    else:
        tries -= 1
        if tries > 0:
            print(f"The static gets louder. Try again, be careful. ({tries} tries left.)")
        else:
            print("The static drowns everything, you can't hear kakau anymore.")

riddle2 = input("\nBlue moon, yellow grass, purple sky, what color is the sun when you're in love?\n> ")
if riddle2.strip().lower() == "white":
    print("The sky hums a lullaby. A door opens, glowing faintly.")
    score += 1
else: 
    print("The sun sight, the door flickers.")

riddle3 = input("\n'I only wisper in you dreams. I only glow when you're sad. I only exist in your name. Who im I?\n> ")
if riddle3.strip().lower() == "kakau":
    print("A sparkle, a laught. A kiss lands in you cheek like mist.")
    score += 1
else:
    print("A tear rolls backwards. He's waiting, still.")

print(f"\nDream dissolving... You solved {score} /3 riddles.")

if score == 3:
    print("You open your eyes and Kakau is there, holding your face gently. He seems reliefed.")
    print("He kisses you, and for once nothing is strange.")
elif score == 2:
    print("You hear his voice behind a wall. So close, yet so far...")
elif score == 1:
    print("You see his silhouette, blurry in the static.")
else:
    print("You're alone, but a faint warmth lingers on your lips.")

#python cocoa.py