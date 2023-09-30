import random

computer_wins = 0
user_wins = 0

game_options = ["rock","paper","scissors"]

while True:

    user_input = input("Type Rock/Paper/Scissors or Q to quit the game: ").lower()

    if user_input == "q":
        quit()
    
    if user_input not in game_options:
        continue

    random_number  = random.randint(0,2)
    # rock : 0 paper : 1 scissors : 2
    computer_pick = game_options[random_number]
    print("Computer picked ",computer_pick,"." )


    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    elif user_input == computer_pick:
        print("Draw!")
    else:
        print("Computer won!")
        computer_wins += 1

    print("You won ",user_wins," times!")
    print("Computer won ",computer_wins," times!")   




