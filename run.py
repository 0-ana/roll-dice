import random

def roll_dice():
    """
    Simulates rolling a six-sided dice, get a random number 1-6.
    """
    return random.randint(1, 6)

def player_turn(player):
    """
    Handles a single player's turn. The player rolls the die repeatedly until they
    either roll a 1 (ending their turn with 0 points) or choose to 'hold' (adding their
    turn total to their overall score).
    """
    turn_total = 0
    while True:
        roll = roll_dice()
        print(f"Player {player} rolled a {roll}")
        if roll == 1:
            print(f"Player {player} rolled a 1! No points added.")
            return 0  # Turn ends with 0 points
        turn_total += roll
        print(f"Player {player}'s turn total is {turn_total}")
        hold = input("Do you want to hold? (y/n): ")
        if hold.lower() == 'y':
            break  # Player chooses to hold and end their turn
    return turn_total

def display_rules():
    """
    Displays the rules of the Pig dice game.
    """
    rules = """
    Welcome to the Roll dice game!

    Rules:
    1. Players take turns to roll a single die as many times as they wish.
    2. Each roll adds the result to the player's turn total.
    3. If a player rolls a 1, their turn total becomes 0, and their turn ends.
    4. A player can choose to 'hold' their turn total, adding it to their overall score, and pass the turn to the next player.
    5. The first player to reach or exceed 100 points wins the game.

    Press Enter to start the game.
    """
    print(rules)
    input()  # Wait for the player to press Enter

def main():
    """
    Main function to run the Roll dice game. Initializes scores, manages player turns,
    and determines the winner when a player reaches the winning score.
    """
    display_rules()  # Display the rules before starting the game

    winning_score = 100
    player_scores = {1: 0, 2: 0}  # Dictionary to track scores for both players
    current_player = 1  # Player 1 starts first

    while player_scores[1] < winning_score and player_scores[2] < winning_score:
        print(f"\nPlayer {current_player}'s turn:")
        turn_total = player_turn(current_player)
        player_scores[current_player] += turn_total
        print(f"Player {current_player}'s total score is now {player_scores[current_player]}")
        
        # Check if the current player has reached the winning score
        if player_scores[current_player] >= winning_score:
            print(f"\nPlayer {current_player} wins with a score of {player_scores[current_player]}!")
            break
        
        # Switch to the other player
        current_player = 2 if current_player == 1 else 1

if __name__ == "__main__":
    main()
