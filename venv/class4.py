# A rock paper scissor game in python
import random
from termcolor import colored
print(colored("Welcome to Rock, paper and scissors game! ","magenta"),"\n\nYour choices are :\n1. Rock\n2. Paper\n3. Scissor")

i = input("Enter number of matches you want to play with pc :")

while True:
    if i == "":
        i = input("Cannot be empty, enter number of matches again :")
    elif i.isdigit() == False:
        i = input("Can only be digits, enter number of matches again :")
    else:
        i = int(i)
        break

user_score = 0
comp_score = 0
list = ["rock", "scissor", "paper"]

print("Lets start the game...\n")

a = 1

while a <= i:
    user_choice = input("Your choice : ")
    comp_choice = random.randint(0, 2)
    if user_choice.lower() == "rock":
        a=a+1
        if (list[comp_choice] == "scissor"):
            print("Computer shows", list[comp_choice])
            user_score = user_score + 1
            print(colored("You won\n Your score = " +  user_score.__str__()+"\n Computer score = " + comp_score.__str__(),"green"))
        elif (list[comp_choice] == "paper"):
            print("Computer shows", list[comp_choice])
            comp_score = comp_score + 1
            print(colored("You Lose\n Your score = " + user_score.__str__() + "\n Computer score = "+ comp_score.__str__(), "red"))
        else:
            print("Computer shows", list[comp_choice])
            print(colored("Its a tie\n Your score = " + user_score.__str__()+ "\n Computer score = " + comp_score.__str__(),"yellow"))
    elif user_choice.lower() == "paper":
        a=a+1
        if (list[comp_choice] == "rock"):
            print("Computer shows", list[comp_choice])
            user_score = user_score + 1
            print(colored("You won\n Your score = " +  user_score.__str__()+"\n Computer score = " + comp_score.__str__(),"green"))
        elif (list[comp_choice] == "scissor"):
            print("Computer shows", list[comp_choice])
            comp_score = comp_score + 1
            print(colored("You Lose\n Your score = " + user_score.__str__() + "\n Computer score = "+ comp_score.__str__(), "red"))
        else:
            print("Computer shows", list[comp_choice])
            print(colored("Its a tie\n Your score = " + user_score.__str__()+ "\n Computer score = " + comp_score.__str__(),"yellow"))
    elif user_choice.lower() == "scissor":
        a=a+1
        if (list[comp_choice] == "paper"):
            print("Computer shows", list[comp_choice])
            user_score = user_score + 1
            print(colored("You won\n Your score = " +  user_score.__str__()+"\n Computer score = " + comp_score.__str__(),"green"))
        elif (list[comp_choice] == "rock"):
            print("Computer shows", list[comp_choice])
            comp_score = comp_score + 1
            print(colored("You Lose\n Your score = " + user_score.__str__() + "\n Computer score = "+ comp_score.__str__(), "red"))
        else:
            print("Computer shows", list[comp_choice])
            print(colored("Its a tie\n Your score = " + user_score.__str__()+ "\n Computer score = " + comp_score.__str__(),"yellow"))
    else:
       print("Wrong choice")

if user_score > comp_score:
    print(colored(" Congratulations you won!","green",attrs=["reverse"]))
else:
    print(colored("\n\n Sorry, you lose", "red", attrs=["reverse"]))

