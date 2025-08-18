def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")

def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([spot == player for spot in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0] == board == board == player:
        return True
    if board == board == board == player:
        return True
    return False

def check_draw(board):
    return all([cell != " " for row in board for cell in row])

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn.")
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
            if board[row][col] != " ":
                print("Spot already taken. Try again.")
                continue
            board[row][col] = player
        except (ValueError, IndexError):
            print("Invalid input. Try again.")
            continue

        if check_win(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        turn += 1

if __name__ == "__main__":
    main()
