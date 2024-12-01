def display_board(board):
    for row in board:
        print("+-------" * 3 + "+")
        print("|       " * 3 + "|")
        print("|   " + "   |   ".join(row) + "   |")
        print("|       " * 3 + "|")
    print("+-------" * 3 + "+")

def enter_move(board):
    while True:
        try:
            move = int(input("Введіть число (1-9): "))
            if 1 <= move <= 9:
                row, col = divmod(move - 1, 3)
                if board[row][col] not in ['X', 'O']:
                    board[row][col] = 'O'
                    break
                else:
                    print("Клітинка вже зайнята. Спробуйте ще раз.")
            else:
                print("Неправильний ввід. Спробуйте ще раз.")
        except ValueError:
            print("Неправильний ввід. Спробуйте ще раз.")

def make_list_of_free_fields(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:
                free_fields.append((row, col))
    return free_fields

def victory_for(board, sign):
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for condition in win_conditions:
        if all(board[r][c] == sign for r, c in condition):
            return True
    return False

def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = free_fields[0]
        board[row][col] = 'X'

def main():
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    board[1][1] = 'X'
    while True:
        display_board(board)
        enter_move(board)
        if victory_for(board, 'O'):
            display_board(board)
            print("Вітаю! Ти вийграв!")
            break
        if not make_list_of_free_fields(board):
            display_board(board)
            print("Нічия")
            break
        draw_move(board)
        if victory_for(board, 'X'):
            display_board(board)
            print("Комп'ютер вийграв!")
            break

if __name__ == "__main__":
    main()