import random

unlucky_numbers = [9, 14, 21, 29]
skip_turn = [11, 15, 23, 27]

print("Welcome to 双六 (sugoroku)! Press 's' to start the game.")
start = input()

if start != "s":
    print("Invalid key. Exiting game.")
    exit()

print("Game has started. The goal is to reach position 30!")

# Initialize player positions
player_pos = 1
computer_pos = 1
goal = 30

# Skip flags
player_skip = False
computer_skip = False

def roll_dice():
    return random.randint(1, 6)

# Game loop
while True:
    # Player turn
    if not player_skip:
        input("Your turn! Press 'r' to roll the dice: ")
        player_roll = roll_dice()
        player_pos += player_roll
        print(f"You rolled a {player_roll}. Your position is now {player_pos}.")

        if player_pos in unlucky_numbers:
            player_pos -= 3
            print("Oh no! You hit an unlucky number! Go back 3 spaces.")
            print(f"Your position is now {player_pos}.")

        if player_pos in skip_turn:
            player_skip = True
            print("You landed on a skip-turn space. You'll skip your next turn.")
    else:
        print("You skip this turn.")
        player_skip = False

    if player_pos >= goal:
        print("You win!")
        break

    # Computer turn
    if not computer_skip:
        print("Computer's turn...")
        computer_roll = roll_dice()
        computer_pos += computer_roll
        print(f"Computer rolled a {computer_roll}. Computer's position is now {computer_pos}.")

        if computer_pos in unlucky_numbers:
            computer_pos -= 3
            print("Computer hit an unlucky number. Goes back 3 spaces.")
            print(f"Computer's position is now {computer_pos}.")

        if computer_pos in skip_turn:
            computer_skip = True
            print("Computer landed on a skip-turn space. Skipping next turn.")
    else:
        print("Computer skips this turn.")
        computer_skip = False

    if computer_pos >= goal:
        print("Computer wins!")
        break


