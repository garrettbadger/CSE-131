# 1. Name:
#      Garrett Badger
# 2. Assignment Name:
#      Lab 05 : Sudoku Draft
# 3. Assignment Description:
#      This program is meant to allow a player to play digital sudoku with error checking
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of this assignment was actually getting the board to display properly in the right format.
# 5. How long did it take for you to complete the assignment?
#      4 hours
import json

def main():
    filename = input("Please input a filename: ")
    board = read_board(filename)
    display_board(board)
    done = ''
    while done != 'q':
        done = play_round(board)
        if done == 'q':
            write_board(last_board)
            break
        display_board(board)
        last_board=board
    

def read_board(filename):
    try:
        file = open('W05/'+filename, 'r')
        board_text = file.read()
        board_json = json.loads(board_text)
        return board_json['board']
    except:
        print('Filename was not vaild.')
    
def display_board(board):
    print('   A B C D E F G H I')
    for row in range(0,9,1):
        if row == 3 or row == 6:
            print('   -----+-----+-----')
            print(f'{row + 1}  ', end="")
        else:
            print(f'{row + 1}  ', end="")
        for column in range(0,9,1):
            seperator = '  |  |  \n'
            if board[row][column] == 0:
                print(" ", end="")
            else:
                print(f'{board[row][column]}', end="")
            print(f'{seperator[column]}', end="")
    
def play_round(board):
    coordinate = input("Specify a coordinate to edit or 'Q' to save and quit or 'S' to see possible moves.\n> ")
    coordinate = coordinate.lower()
    if coordinate == 'q':
        return 'q'
    if coordinate == 's':
        point = input('Which coordinate would you like to see moves for? ')
        possible_moves(board, point)
        return
    number = int(input(f"What number goes in {coordinate.upper()}? "))
    row, column = parse_input(coordinate.upper())
    legal = is_input_legal(board, number, row, column)
    if legal:
        board[row][column] = number

def possible_moves(board, co):
    row, column = parse_input(co.upper())
    non_moves = set()
    print(f'Your possible moves for {co} are: ')
    for i in board[row]:
            non_moves.add(i)
    for i in range(0,9,1):
        non_moves.add(board[i][column])
    if row < 3:
        if column < 3:
            for i in range(3):
                for x in range(3):
                    non_moves.add(board[i][x])
        if column < 6 and column > 3:
            for i in range(3):
                for x in range(3, 6):
                    non_moves.add(board[i][x])
        if column < 9 and column > 6:
            for i in range(3):
                for x in range(6, 9):
                    non_moves.add(board[i][x])
    if row < 6 and row > 3:
        if column < 3:
            for i in range(3, 6):
                for x in range(3):
                    non_moves.add(board[i][x])
        if column < 6 and column > 3:
            for i in range(3, 6):
                for x in range(3, 6):
                    non_moves.add(board[i][x])
        if column < 9 and column > 6:
            for i in range(3, 6):
                for x in range(6, 9):
                    non_moves.add(board[i][x])
    if row < 9 and row > 6:
        if column < 3:
            for i in range(6, 9):
                for x in range(3):
                    non_moves.add(board[i][x])
        if column < 6 and column > 3:
            for i in range(6, 9):
                for x in range(3, 6):
                    non_moves.add(board[i][x])
        if column < 9 and column > 6:
            for i in range(6, 9):
                for x in range(6, 9):
                    non_moves.add(board[i][x])
            

    for i in range(0,9,1):
            if i not in non_moves:
                print(i)
    print()
    
def parse_input(coordinate):
    for letter in coordinate:
        if 'A' <= letter <= 'Z':
            column = ord(letter) - ord('A')
        if '1' <= letter <= '9':
            row = int(letter) - 1
    return(row, column)
    
def is_input_legal(board, number, row, column):
    valid = 0
    inside_square = 0
    if number < 1 or number > 9:
        print('Number is invalid. Needs to be in-between 1-9.')
        return False
    if board[row][column] != 0:
        print('This square is not empty. Choose another square.')
        return False
    if number not in board[row]:
        for i in range(0,9,1):
            if number != board[i][column]:
                valid += 1
            else:
                print('The number you entered earlier is already in the column.')
    else:
        print('The number you entered earlier is already in the row.')
    if row < 3:
        if column < 3:
            for i in range(3):
                for x in range(3):
                   if number != board[i][x]:
                       inside_square +=1
        if column < 6 and column > 3:
            for i in range(3):
                for x in range(3, 6):
                    if number != board[i][x]:
                       inside_square +=1
        if column < 9 and column > 6:
            for i in range(3):
                for x in range(6, 9):
                    if number != board[i][x]:
                       inside_square +=1
    if row < 6 and row > 3:
        if column < 3:
            for i in range(3, 6):
                for x in range(3):
                   if number != board[i][x]:
                       inside_square +=1
        if column < 6 and column > 3:
            for i in range(3, 6):
                for x in range(3, 6):
                  if number != board[i][x]:
                       inside_square +=1
        if column < 9 and column > 6:
            for i in range(3, 6):
                for x in range(6, 9):
                   if number != board[i][x]:
                       inside_square +=1
    if row < 9 and row > 6:
        if column < 3:
            for i in range(6, 9):
                for x in range(3):
                   if number != board[i][x]:
                       inside_square +=1
        if column < 6 and column > 3:
            for i in range(6, 9):
                for x in range(3, 6):
                   if number != board[i][x]:
                       inside_square +=1
        if column < 9 and column > 6:
            for i in range(6, 9):
                for x in range(6, 9):
                   if number != board[i][x]:
                       inside_square +=1
    if valid == 9 and inside_square == 9:
        return True
    else: 
        print('The number you entered is already in the inside square.')
        return False
        
def write_board(board):
    filename = input("Please enter a valid filename: ")
    with open('W05/'+filename, 'w') as file:
        board_json = {}
        board_json['board'] = board
        board_text = json.dumps(board_json)
        file.write(board_text)
        file.close()
    
if __name__ == "__main__":
    main()