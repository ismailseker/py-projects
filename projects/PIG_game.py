import random

def roll():
    min_value = 1
    max_value = 6

    roll = random.randint(min_value,max_value)

    return roll

while True:
    players = input("Enter the players number: ")

    if players.isdigit():
        players = int(players)
        break
    else:
        print("Please enter a digit. Try again !")

max_score = 60
players_scores = [0 for _ in range(players)]

while max(players_scores) < max_score:
    for player_idx in range(players):
        print("\n Player number", player_idx + 1,"turn has just started.!")
        print("Your total score is: ",players_scores[player_idx],"\n")
        current_score = 0


        while True:
            ask_roll = input("Would you like to roll ? (yes)")
            
            if ask_roll.lower() != "yes":
                break
            
            value = roll()
            
            if value == 1:
                print("You rolled 1, Your turn is over !")
                current_score = 0
                break
            else:
                current_score += value
                print("Your score is: ", current_score)

        players_scores[player_idx] += current_score
        print("Your total score is: ",players_scores[player_idx])

max_score = max(players_scores)
winning_idx = players_scores.index(max_score)
print("Player number ",winning_idx + 1 ,"is the winner with a score of:", max_score)
                



