import random

# Define the snake and ladder positions to move upwards or downwards in the board
snake_ladder = {
    4: 14,
    9: 31,
    17: 7,
    20: 38,
    28: 84,
    35: 13,
    40: 59,
    51: 67,
    54: 34,
    62: 19,
    63: 81,
    64: 60,
    71: 91,
    87: 24,
    93: 73,
    95: 75,
    99: 78
}

# Define the player positions and number of players
num_players = int(input("Enter Number of players want to play Snake and Ladder: "))
player_positions = [0] * num_players

# Define a function to roll the die and move the player
def roll_die():
    return random.randint(1, 6)

def move_player(player, spaces):
    player_positions[player] += spaces
    if player_positions[player] in snake_ladder:
        player_positions[player] = snake_ladder[player_positions[player]]

# Define the game loop
game_over = False
current_player = 0
while not game_over:
    # Roll the die and move the player
    input(f"Player {current_player + 1}, press enter to roll the die")
    spaces = roll_die()
    print(f"Player {current_player + 1} rolled a {spaces}")
    move_player(current_player, spaces)
    
    if player_positions[current_player] < 100:
        print(f"Player {current_player + 1} is at a position {player_positions[current_player]}")
    print("===================================================================================")
    # Check for win condition
    if player_positions[current_player] >= 100:
        print(f"****Player {current_player + 1} has won!!!!!****")
        game_over = True
        break

    # Switch to the next player
    current_player = (current_player + 1) % num_players
