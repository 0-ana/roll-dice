import random
from colorama import Fore, Style
import pyfiglet


def roll_dice():
    """
    Simulates rolling a six-sided dice, get a random number 1-6.
    """
    return random.randint(1, 6)


def player_turn(player):
    """
    Handles a single player's turn. The player rolls the die repeatedly until
    they either roll a 1 (ending their turn with 0 points) or choose to 'hold'
    (adding their turn total to their overall score).
    """
    turn_total = 0
    while True:
        # Roll the die
        roll = roll_dice()
        print(f"Player {player} rolled a {roll}")
        # Check if the roll is 1
        if roll == 1:
            print(f"\nPlayer {player} rolled a 1! No points added.")
            return 0  # Turn ends with 0 points
        turn_total += roll  # Add the roll value to the turn total
        print(f"\nPlayer {player}'s turn total is {turn_total}")

        # Loop to ensure valid input ('y' or 'n')
        while True:
            hold = input("Do you want to hold? (y/n): ").strip().lower()
            if hold in ['y', 'n']:
                break  # Exit the loop if the input is valid
            else:
                print("\nInvalid! Enter 'y' to hold or 'n' to continue.")

        # Check if the player chooses to hold
        if hold == 'y':
            break  # Player chooses to hold and end their turn
    return turn_total


def display_rules():
    """
    Displays the rules of the Pig dice game.
    """
    # Reset color
    print(Style.RESET_ALL)
    # Display a welcome message
    welcome = pyfiglet.figlet_format("Welcome  to  Roll  Dice  Game !")
    rules = """
    Rules:
    1. Players take turns to roll a single die as many times as they wish.
    2. Each roll adds the result to the player's turn total.
    3. If a player rolls a 1, their turn total becomes 0, and their turn ends.
    4. A player can choose to 'hold' their turn total, adding it to their
       overall score, and pass the turn to the next player.
    5. The first player to reach or exceed 50 points wins the game.

    Press Enter to start the game.
    """
    print(welcome)
    print(rules)
    input("Press Enter to start...")  # Wait for the player to press Enter


def main():
    """
    Main function to run the Roll dice game. Initializes scores,
    manages player turns, and determines the winner when a player
    reaches the winning score.
    """
    # Loop to allow replaying the game
    while True:
        display_rules()  # Display the rules before starting the game
        winning_score = 50  # Set a goal
        player_scores = {1: 0, 2: 0}  # Track scores for both players
        current_player = 1  # Player 1 starts first

        # Loop until one of the players reaches the winning score
        while (player_scores[1] < winning_score and
               player_scores[2] < winning_score):
            if current_player == 1:
                # Player 1's turn in red
                print(Fore.RED + f"\nPlayer {current_player}'s turn:")
            else:
                # Player 2's turn in blue
                print(Fore.BLUE + f"\nPlayer {current_player}'s turn:")

            # Execute the player's turn
            turn_total = player_turn(current_player)
            # Update the player's total score
            player_scores[current_player] += turn_total
            # Display the updated score
            print(f"\nPlayer {current_player}'s total score is now "
                  f"{player_scores[current_player]}")
            # Check if the current player has reached the winning score
            if player_scores[current_player] >= winning_score:
                # Display the winner and winner's score
                print(f"\nPlayer {current_player} wins with a score of "
                      f"{player_scores[current_player]}!")
                break
            # Switch to the other player
            current_player = 2 if current_player == 1 else 1

        # Ask if players want to play again
        while True:
            # Reset color
            print(Style.RESET_ALL)
            play_again = input("Do you want to play again? (y/n): "
                               ).strip().lower()
            if play_again in ['y', 'n']:
                break  # Exit the loop if the input is valid
            else:
                print("\nInvalid input. Please enter 'y' to play again or "
                      "'n' to exit.")

        # Check if the players want to exit
        if play_again == 'n':
            goodbye = pyfiglet.figlet_format("Thanks  for  playing! Goodbye!")
            print(goodbye)
            break  # Exit the main loop and end the program


if __name__ == "__main__":
    main()
