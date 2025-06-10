import random

youcdict = {
    "stone": 1,
    "paper": -1,
    "scissors": 0
}

you = input("Enter your choice (stone, paper, scissors): ").lower()

if you not in youcdict:
    print("Invalid choice. Please enter stone, paper, or scissors.")
else:
    def is_winner(you, com):
        return (you == "stone" and com == "scissors") or \
               (you == "paper" and com == "stone") or \
               (you == "scissors" and com == "paper")

    com = random.choice(["stone", "paper", "scissors"])
    print(f"Computer chose: {com}")
    
    if you == com:
        print("It's a tie!")
    elif is_winner(you, com):
        print("You win!")
    else:
        print("You lose!")
