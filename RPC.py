import random

computer = random.choice(["rock", "paper", "scissors"])

user = input("rock, paper or scissors? ")

print("The computer chose", computer,"and the user chose", user +".")
if user == computer:
    print("Its a tie")
elif user == "rock" and computer == "scissors":
    print("You win")
elif user == "scissors" and computer == "paper":
    print("You win")
elif user == "paper" and computer == "rock":
    print("You win")
else: print("You lose")

# TODO - Implement the if statements that prints who wins