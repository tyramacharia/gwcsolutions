start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''

print(start)

user_input = ""

#while loop checks for valid user input
while user_input != "left" and user_input != "right":
    print("Type 'left' to go left or 'right' to go right")
    user_input = input()

if user_input == "left":
    print("You decide to go left and you run into a wall and die.")
elif user_input == "right":
    print("You choose to go right and run into a giant snake. Should you run away or make friends with the snake?")

    #while loop checks for valid user input
    while user_input != "run away" and user_input != "make friends":
        print("Type 'run away' or 'make friends'")
        user_input = input()

    if user_input == "run away":
        print("The snake caught up with you and bites you. You  died.")
    elif user_input == "make friends":
        print("The snake appreciated your kindness and let you out of the maze! Congrats you are saved!!")
