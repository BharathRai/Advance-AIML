def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")

def check_win(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(cell != " " for row in board for cell in row)

def score_board(board):
    if check_win(board, "O"):  # AI
        return +1
    elif check_win(board, "X"):  # Human
        return -1
    return 0

def minimax(board, depth, is_maximizing):
    score = score_board(board)

    # Terminal state
    if score != 0 or check_draw(board):
        return score

    if is_maximizing:
        best_score = -999
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best_score = max(best_score, minimax(board, depth+1, False))
                    board[i][j] = " "
        return best_score
    else:
        best_score = 999
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best_score = min(best_score, minimax(board, depth+1, True))
                    board[i][j] = " "
        return best_score

def best_move(board):
    best_score = -999
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)

        # Human turn
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
            if board[row][col] != " ":
                print("Spot already taken. Try again.")
                continue
            board[row][col] = "X"
        except (ValueError, IndexError):
            print("Invalid input. Try again.")
            continue

        if check_win(board, "X"):
            print_board(board)
            print("Player X wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI turn
        print("AI is thinking...")
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = "O"

        if check_win(board, "O"):
            print_board(board)
            print("AI (O) wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
