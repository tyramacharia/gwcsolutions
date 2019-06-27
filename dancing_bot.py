import random

dance_list = ["~dab~", "~macarena~", "~shoot~", "~sprinkler~"]

def intro():
    print("hi welcome! im a dancing bot! ")

def dab():
    print("~hits the dab~")

def macarena():
    print("dale a tu cuerpo alegría macarena\nheeyyy macarena!")

def shoot():
    print("shoot!! shoot!! shooot!!")

def say_hi():
    print("hello")

def say_bye():
    print("see you next time!")

def do_a_dance():
    for i in range(6):
        print(random.choice(dance_list))

def say_default():
    print("thats cool")

def process_input(answer):
    if answer == "say hi":
        say_hi()
    elif answer == "dab":
        dab()
    elif answer == "shoot":
        shoot()
    elif answer == "macarena":
        macarena()
    elif answer == "do a dance":
        do_a_dance()
    elif answer == "stop":
        say_bye()
        return True
    else:
        say_default()


def main():
    intro()
    done = False
    while not done:
        print()
        answer = input("what should i do? (enter 'do a dance', 'dab', 'shoot', 'macarena' or 'stop')")
        done = process_input(answer)

if __name__ == "__main__":
    main()
