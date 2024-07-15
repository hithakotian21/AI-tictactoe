import math

# Define the board
board = [' ' for _ in range(9)]

def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def check_winner(board, player):
    # Check rows, columns and diagonals
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                      (0, 4, 8), (2, 4, 6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

def is_board_full(board):
    return ' ' not in board

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

def best_move(board):
    best_val = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            move_val = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = ' '
            if move_val > best_val:
                best_val = move_val
                move = i
    return move

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()
    
    while True:
        # Human move
        while True:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if board[move] == ' ':
                    board[move] = 'X'
                    break
                else:
                    print("Invalid move. Try again.")
            except (IndexError, ValueError):
                print("Invalid input. Enter a number between 1 and 9.")
        
        print_board()
        
        if check_winner(board, 'X'):
            print("Congratulations! You won!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break
        
        # AI move
        ai_move = best_move(board)
        board[ai_move] = 'O'
        print("AI makes a move:")
        print_board()
        
        if check_winner(board, 'O'):
            print("AI wins! Better luck next time.")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()
