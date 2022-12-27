from random import choice

game_state = {"R": "Rock", "P": "Paper", "S": "Scissors"}
options = list(game_state.keys())
winnings = ["RS", "PR", "SP"]
result = "{0} beats {1}"

while True:
    computer = choice(options)
    player = input("Enter R for Rock , P for Paper, S for Scissors, and, done to quit the game: ").upper()

    match [player, f'{player}{computer}', computer]:
        case ["R" | "S" | "P", move, computer] if computer == player:
            print("It is a tie! Try again.")

        case ["R" | "S" | "P", move, computer]:
            winner, winner_move, looser_move = ("Player", player, computer) if move in winnings else ("Computer", computer, player)
            print(f"{winner} won")
            print(result.format(game_state[winner_move], game_state[looser_move]))

        case ['DONE' | "END" | "STOP", _, _]:
            print("Game Over")
            break

        case [player, _, _]:
            print(f"{player} is not a valid option. Enter a valid option")
