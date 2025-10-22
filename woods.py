
print("You wake up in a weird open camp, its evening and the night is coming. You see an flickering flashlight right beside you.")

choice1 = input("Do you pick up the lantern? (yes/no)\n> ")

if choice1.strip().lower() == "yes":
    print("You picked up the lantern, a faint white glow illuminates an open path between the grass.")
else:
    print("You leave the lantern, its so dark... You trip over something and hear a whisper, weird...")

print("You take a few steps foward and see two wooden cabins, one with the door half open and the other one with the door closed.")

choice2 = input("Do you choose the the cabin with which door? (half open/closed/none) \n> ")

if choice2.strip().lower() == "half open":
    print("You see and old lady by an old fireplace, she offers you a cup of tea and a bed for the night.")

elif choice2.strip().lower() == "closed":
    print("You can't open the door, but you can see throught the window, someone looking at you.")
    phrase = input("Strange tall man: What do you want?\n> ")
    if phrase.strip().lower() == "stay for the night":
        print("Strange tall old man: Alright mate, but if you try something I will kill you.")
    else:
        print("Strange tall old man: Get the hell out of here, mate. I'll say this just one time.")

elif choice2.strip().lower() == "none":
    print("You kept walking, leaving both cabins away and die before the daylight arrives.")

else: 
    print("You kept walking, leaving both cabins away and dies before the daylight arrives.")

#python woods.py