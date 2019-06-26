import random

# A list of words that
potential_words = ["example", "words", "someone", "can", "guess"]

#randomly selects a word
word = random.choice(potential_words)

# Use to test your code:
current_word = []

# TIP: the number of letters should match the word

# Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
for i in range(len(word)):
    current_word.append("_")
print(current_word)

# Some useful variables
guesses = []
max_fails = 5
fails = 0

while fails < max_fails:
    correct = False
    while True:	#Check if the guess is valid: Is it one letter? Have they already guessed it?
        print("Guess a letter: ")
        guess = input()
        if len(guess) != 1:
            print("Please only enter one letter at a time.")
            continue
        elif guess in guesses:
            print("You have already entered that letter. Please guess another letter.")
            continue
        else:
            break

    guesses.append(guess) #if guess is valid append it to the list guesses

    for i in range(len(word)): # check if the guess is correct: Is it in the word? If so, reveal the letters!
        if guess == word[i]:
            current_word[i] = word[i]
            correct = True

    print(current_word)

    if "_" not in current_word: #checks to see if there are any blanks left, if not the player wins
        print("Congrats you have guesses it!!")
        break

    if not correct:
        fails = fails + 1
        print("You have " + str(max_fails - fails) + " tries left!")
