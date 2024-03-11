#Explain: each player picks num from board   of numbers between 1 and 9. Each player takes
#"""turns picking a number from the list. Once a number has been picked, it cannot be pickedagain. If a player has picked three numbers that add up to 15, that player wins the game.
#However, if all the numbers are used and no player gets exactly 15, the game is a draw.

# Name : Abelrahman Mohsen Ahmed El-noby
# File: CS112_A1_T2_2_20231097
# ID : 20231097 

import random

def the_board(numbers):
    print("Remaining numbers on the board:", numbers)

def check_winner(player_picks):
    # Check if the player has three numbers that add up to 15
    if len(player_picks) < 3:
        return False
    for pick1 in range(len(player_picks)):
        for pick2 in range(pick1+1, len(player_picks)):
            for pick3 in range(pick2+1, len(player_picks)):
                if player_picks[pick1] + player_picks[pick2] + player_picks[pick3] == 15:
                    return True
    return False

def number_scrabble():
    print("**** Welcome to Number Scrabble! ****\n")
    input("Press Enter to start the game.")

    while True:
        # Get names from user 
        player1_name = input("Enter Player 1's name: ")
        player2_name = input("Enter Player 2's name: ")

        # Set the board with numbers from 1 to 9
        board = list(range(1, 10))
        player1_picks = []
        player2_picks = []

        # Determine starting player randomly to make the game have some fairness
        starting_player = random.choice([player1_name, player2_name])
        print(f"{starting_player} will start the game.")
        current_player = starting_player


        player_won = False

    
        for turn in range(9):
            print("\n")
            # Display the updated board each turn 
            the_board(board)  

            # User input and when using try and except prevent any wrong input from user 
            while True:
                try:
                    chosen_number = int(input(f"{current_player}, choose a number: "))
                    if chosen_number not in board:
                        print("Number not available on the board. Please choose a number from the remaining numbers.")
                        continue

                    # Remove the chosen number from the board
                    board.remove(chosen_number)

                    # Update picks 
                    if current_player == player1_name:
                        player1_picks.append(chosen_number)
                        if check_winner(player1_picks):
                            print(f"Congratulations, {player1_name}! You win!")
                            player_won = True
                            break
                    else:
                        player2_picks.append(chosen_number)
                        if check_winner(player2_picks):
                            print(f"Congratulations, {player2_name}! You win!")
                            player_won = True
                            break

                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            if player_won:
                break

            # Switch to the other player
            current_player = player2_name if current_player == player1_name else player1_name
        else:
            print("It's a draw! No player gets a combination adding up to 15.")

        # Ask if the players want to play again
        play_again = input("Press Enter to play again or type 'exit' to quit: ")
        if play_again.lower() == 'exit':
            break

# Call the game function to start playing
number_scrabble()