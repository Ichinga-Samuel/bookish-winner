from random import choice

game_state = {"R": "Rock", "P": "Paper", "S": "Scissors"}
options = list(game_state.keys())
winnings = ["RS", "PR", "SP"]
result = "{0} beats {1}"

while True:
    computer = choice(options)
    player = input("Enter R for Rock , P for Paper, S for Scissors, and, done to quit the game: ").upper()

    if player == "DONE":
        print("Game Over")
        break

    elif player not in options:
        print("Wrong choice, Pick again. Rock, Paper or Scissors?")
        continue

    elif player == computer:
        print("Tie!, Here we go again!")
        continue

    else:
        move = player+computer
        winner, winner_move, looser_move = ("Player", player, computer) if move in winnings else ("Computer", computer, player)
        print(f"{winner} Won!", result.format(game_state[winner_move], game_state[looser_move]))
