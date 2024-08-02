import random

def roll_dice():
    """
    Simulates rolling a six-sided dice, get a random number from 1 to 6
    """
    return random.randint(1,6)
    
def player_turn(player):
    """
    Handles a single player's turn. The player rolls the die repeatedly until they
    either roll a 1 (ending their turn with 0 points) or choose to 'hold' (adding their
    turn total to their overall score)

    """
    turn_total = 0
    while True:
        roll = roll_dice()
        print(f"Player {player} rolled a {roll}.")
        if roll == 0:
            print(f"Player {player} rolled a 1! No point added.")
            return 0 #Turn ends with 0 points
        turn_total +=roll
        print(f"Player {player}'s turn total is {turn_total}")
        hold = input("Do you want to hold?(y/n):")
        if hold.lower() == 'y':
            break #Player chooses to hold and end their turn
        return turn_total