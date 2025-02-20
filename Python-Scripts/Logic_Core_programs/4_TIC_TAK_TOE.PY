import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

def get_computer_move(board):
    while True:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if board[row][col] == " ":
            return row, col

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    for turn in range(9):
        print_board(board)
        if turn % 2 == 0:
            print("Computer's turn:")
            row, col = get_computer_move(board)
            board[row][col] = "O"
        else:
            while True:
                try:
                    row, col = map(int, input("Enter row and column (0-2) separated by space: ").split())
                    if board[row][col] == " ":
                        board[row][col] = "X"
                        break
                    else:
                        print("Cell already occupied. Try again.")
                except (ValueError, IndexError):
                    print("Invalid input. Enter row and column between 0 and 2.")
        
        if check_winner(board, "O"):
            print_board(board)
            print("Computer wins!")
            return
        elif check_winner(board, "X"):
            print_board(board)
            print("You win!")
            return
    
    print_board(board)
    print("It's a draw!")

tic_tac_toe()