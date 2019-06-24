#importing all functions from the random library
from random import *

#generate random number from 1 to 20 (inclusive)
rand_num = randint(1, 20)
guesses_left = 3

#while loop will continue until there are no guesses left
while guesses_left > 0:
    guess = input("Guess a number between 1 and 20 (inclusive): ")
    #decrements guesses let by 1
    guesses_left -= 1
    if not guess.isnumeric(): # checks if a string is only digits 0 to 9
    	print("That's not a positive whole number, try again!")
    else:
        guess = int(guess) # converts a string to an integer

        if(guess > rand_num): #checks to see if input is too high
            print("Your guess is too high.")
        elif(guess < rand_num): #checks to see if input is too low
            print("Your guess is too low.")
        else: #will be displayed if guess if corret
            print("You guessed correctly!")
            break #breaks while loop

print("the random number is %d" %(rand_num)) #prints correct number
