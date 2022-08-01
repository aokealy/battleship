import random

LENGTH_OF_SHIPS = [2,3,3,4,5] # Length of ships
PLAYER_BOARD = [[" "] * 8 for i in range(8)] #the player board
COMPUTER_BOARD = [[" "] * 8 for i in range(8)] 
PLAYER_GUESS_BOARD = [[" "] * 8 for i in range(8)]
COMPUTER_GUESS_BOARD = [[" "] * 8 for i in range(8)]
LETTERS_TO_NUMBERS = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7} #list for letters to numbers

def print_board(board):
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board: #loop through board
        print("%d|%s|" % (row_number, "|".join(row))) #decimal and string print
        row_number += 1

def place_ships(board):
    # loop through the length of the ships
    for ship_length in LENGTH_OF_SHIPS:
        #loop through until the ship fits and no overlap
        while True:
            if board == COMPUTER_BOARD: #if computer randomly place pieces that fit on board
                orientation, row, column = random.choice(["H", "V"]), random.randint(0, 7), random.randint(0, 7)
                if check_ship_fit(ship_length, row, column, orientation):
                    #check if ship overlaps
                    if ship_overlaps(board, row, column, orientation, ship_length) == False:
                        #place ships
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship_length):
                                board[row][i] = "X"
                        break
            else:
                place_ship = True
                print('Place the ship with a length of ' + str(ship_length))
                row, column, orientation = user_input(place_ship)
                if check_ship_fit(ship_length, row, column, orientation):
                    #check if ship overlaps
                    if ship_overlaps(board, row, column, orientation, ship_length) == False:
                        #place ships
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship_length):
                                board[row][i] = "X"
                        print_board(PLAYER_BOARD)
                        break         

def check_ship_fit(SHIP_LENGTH, row, column, orientation):
    if orientation == "H":
        if column + SHIP_LENGTH > 8:
            return False
        else:
            return True
    else:
        if row + SHIP_LENGTH > 8:
            return False
        else:
            return True           
    

def ship_overlap(board, row, column, orientation, ship_length):
    if orientation == "H":
        for i in range(column, column + ship_length):
            if board[row][i] == "X":
                return True
    else:
        for i in range(row, row + ship_length):
            if board[row][i]  == "X":
                return True
    return False                       
    

def user_input(place_ship):
    if place_ship == True:
        while True:
            try:
                orientation = input("Enter orientation (H or V):").upper() # accepts uppercase and lowercase H or V
                if orientation == "H" or orientation == "V":
                    break
            except TypeError:
                print('Please enter a valid orientation H or V') 
        while True:
            try:
                row = input("Enter the row 1-8 of the battleship: ")
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:
                print('Please enter a valid letter between 1-8')
        while True:
            try:
                column = input("Enter the column of the ship: ").upper()
                if column in 'ABCDEFGH':
                    column = LETTERS_TO_NUMBERS[column]
                    break
            except KeyError:
                print('Enter a valid letter between A-H')
        return row, column, orientation
    else:
        while True:
            try:
                row - input("Enter the row 1-8 of the ship: ")
                if row in '12345678':
                    row = int(row) - 1
                    break
            except KeyError:
                print('Emter a valid letter between A-H') 
        return row, column                                          

def count_hit_ships(board):
    count = 0
    for row in board:
        if column == "X":
            count += 1
    return count
    

def turn(board):
    if board == PLAYER_GUESS_BOARD:
        row, column = user_input(PLAYER_GUESS_BOARD)
        if board[row][column] == "_":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif COMPUTER_BOARD[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] == "_"     


while True:



