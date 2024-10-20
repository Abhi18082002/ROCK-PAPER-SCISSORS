#Using if statements

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


print("Welcome to ROCK PAPER SCISSORS")
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))


if your_choice == 0:
    print("You Choice is Rock")
    print(rock)
elif your_choice == 1:
    print("You Choice is Paper")
    print(paper)
elif your_choice == 2:
    print("You Choice is Scissors")
    print(scissors)
else :
    print("invalid option")

computer_choice = random.randint(0,1)
if computer_choice == 0:
    print("Computer Choose Rock")
    print(rock)
elif computer_choice == 1:
    print("Computer Choose Paper")
    print(paper)
elif computer_choice == 2:
    print("Computer Choose Scissors")
    print(scissors)
else :
    print("invalid option")

if your_choice  == computer_choice:
    print("Results Undeclared")
# elif your_choice >3 or computer_choice <=0 :
#     print("Invalid Option")
elif your_choice == 0 and computer_choice == 1:
    print(" YOU LOOSE")
elif your_choice == 0 and computer_choice == 2:
    print("YOU WIN")
elif your_choice == 1 and computer_choice == 2:
    print("YOU LOOSE")
elif your_choice == 1 and computer_choice == 0:
    print(" YOU WIN")
elif your_choice == 2 and computer_choice == 0:
    print("YOU LOOSE")
elif your_choice == 2 and computer_choice == 1:
    print("YOU WIN")
else :
    print("Results Undeclared")
