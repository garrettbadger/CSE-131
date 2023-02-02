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
    filename = input("Please input a filename: Easy, Medium, Hard:\n> ")
    board = read_board(filename)
    display_board(board)
    while board != 'Q' or board != 'q':
        board = play_round(board)
        if board == 'Q' or board == 'q':
            write_board(filename, last_board)
            break
        display_board(board)
        last_board=board
    

def read_board(filename):
    try:
        file = open('W05/131.05.'+filename+'.json', 'r')
        board_text = file.read()
        board_json = json.loads(board_text)
        return board_json['board']
    except:
        print('Filename was not vaild. Make sure filename is either: Easy, Medium, Hard.')
    
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
    coordinate = input("Specify a coordinate to edit or 'Q' to save and quit\n> ")
    if coordinate == 'Q' or coordinate == 'q':
        return 'Q'
    number = int(input(f"What number goes in {coordinate}? "))
    row, column = parse_input(coordinate)
    legal = is_input_legal(board, number, row, column)
    if legal:
        board[row][column] = number
    return board
    
def parse_input(coordinate):
    for letter in coordinate:
        if 'A' <= letter <= 'Z':
            column = ord(letter) - ord('A')
        if '1' <= letter <= '9':
            row = int(letter) - 1
    return(row, column)
    
def is_input_legal(board, number, row, column):
    valid = 0
    if number not in board[row]:
        for i in range(0,9,1):
            if number != board[i][column]:
                valid += 1
    if valid == 9:
        return True
    else: 
        return False
        
def write_board(filename, board):
    with open('W05/131.05.'+filename+'.json', 'w') as file:
        board_json = {}
        board_json['board'] = board
        board_text = json.dumps(board_json)
        file.write(board_text)
        file.close()
    
if __name__ == "__main__":
    main()