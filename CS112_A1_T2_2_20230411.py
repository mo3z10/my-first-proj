# file:CS112_A1_T2_2_20230411.PY.
# purpose: Each player chooses a number from 1 to 9.
# The chosen number cannot be chosen again. The player who collects three numbers whose sum is 15 wins.
# author: Moaz Yasser Mahmoud Ali
# ID: 20230411
numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
player1 = []
player2 = []

# Function to check if any player has combined three numbers whose sum is 15
def winner(player):
    if len(player) < 3:
        return False

    for i in range(len(player)-2):
        for j in range(i+1, len(player)-1):
            for k in range(j+1, len(player)):
                if player[i] + player[j] + player[k] == 15:
                    return True
    return False

while True:
    # Loop to ask player 1 to choose a number from the available
    print("                 Number Scrabble Game          ")

    while True:
        while True:
            print("The available numbers are", numbers)
            # Check for any error or wrong input
            try:
                p1 = int(input("Player 1, please enter a number: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            if p1 in player1 or p1 in player2 or p1 not in numbers:
                print("Number is invalid. Please enter another number.")
                continue
            # Add the number to the player1 list and remove it from the available
            else:
                numbers.remove(p1)
                player1.append(p1)
                break

        # Call the function to check winner for player 1
        if winner(player1):
            print("Player 1 wins!")
            break

        if len(player1) == 5:
            print("It's a draw!")
            break

        # Take a number from player 2 and check if it's available
        while True:
            print("The available numbers are", numbers)
            try:
                p2 = int(input("Player 2, please enter a number: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            if p2 in player1 or p2 in player2 or p2 not in numbers:
                print("Number is invalid. Please enter another number.")
                continue
            # Add the number to player 2 list and remove it from the available
            else:
                numbers.remove(p2)
                player2.append(p2)
                break

        print("Player 1 =", player1)
        print("Player 2 =", player2)

        # Call the function to check winner for player 2
        if winner(player2):
            print("Player 2 wins!")
            break

        # Check for draw
        if len(player2) == 5:
            print("It's a draw!")
            break

    # After each round, ask the players if they want to play again
    if winner(player1) or winner(player2) or len(player1) == 5:
        print("to play again press 1")
        print("to end the game press any key")
        try :
         choice = int(input("Please choose: "))
        except ValueError:
            break

        if choice == 1:
            # Reset the game state
            numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
            player1 = []
            player2 = []
            continue
        else:
            break
