#pig game
# A simple dice game where players take turns rolling a die to accumulate points.
# The first player to reach a score of 50 wins the game.

import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

max_score = int(input("Enter the maximum score to win (default 50): ") or 50)
player_scores = [0 for score in range(players)]

while max(player_scores) < max_score:
    for player_id in range(players):
        print("\nPlayer number", player_id + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_id], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y or n)? (default y) ") or "y"
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled 1! You lose your turn!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score is:", current_score)

        player_scores[player_id] += current_score
        print("Your total score is:", player_scores[player_id])

max_score = max(player_scores)
winning_id = player_scores.index(max_score)
print("Player number", winning_id + 1,"won the game with a score of:", max_score)