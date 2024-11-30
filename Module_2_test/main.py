# def check_winner():
#     if area[0][0] == 'X' and area[0][1] == 'X' and area[0][2] == 'X':
#         return 'X'
#     if area[0][0] == '0' and area[0][1] == '0' and area[0][2] == '0':
#         return '0'
#     if area[1][0] == 'X' and area[1][1] == 'X' and area[1][2] == 'X':
#         return 'X'
#     if area[1][0] == '0' and area[1][1] == '0' and area[1][2] == '0':
#         return '0'
#     if area[2][0] == 'X' and area[2][1] == 'X' and area[2][2] == 'X':
#         return 'X'
#     if area[2][0] == '0' and area[2][1] == '0' and area[2][2] == '0':
#         return '0'
#     if area[0][0] == 'X' and area[1][0] == 'X' and area[2][0] == 'X':
#         return 'X'
#     if area[0][0] == '0' and area[1][0] == '0' and area[2][0] == '0':
#         return '0'
#     if area[1][0] == 'X' and area[1][1] == 'X' and area[1][2] == 'X':
#         return 'X'
#     if area[1][0] == '0' and area[1][1] == '0' and area[1][2] == '0':
#         return '0'
#     if area[0][0] == 'X' and area[1][1] == 'X' and area[2][2] == 'X':
#         return 'X'
#     if area[0][0] == '0' and area[1][1] == '0' and area[2][2] == '0':
#         return '0'
#     if area[0][2] == 'X' and area[1][1] == 'X' and area[2][0] == 'X':
#         return 'X'
#     if area[0][2] == '0' and area[1][1] == '0' and area[2][0] == '0':
#         return '0'
#     return('*')
# def draw_area():
#     for i in area:
#         print(*i)
# print()
# area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
# print('Welcome to Tic-Tac-Toe')
# print('______________________')
# draw_area()
#
# for turn in range(1, 10):
#     print(f'Your go: {turn}')
#     if turn % 2 == 0:
#         turn_char = '0'
#         print("Nought's go")
#     else:
#         turn_char = 'X'
#         print("Cross' go")
#     row = int(input('Enter row number (1, 2, 3) ')) - 1
#     column = int(input('Enter column number (1, 2, 3) ')) - 1
#     if area[row][column] == '*':
#             area[row][column] = turn_char
#     else:
#         print('Cell busy, no go')
#         draw_area()
#         continue
#     draw_area()
#
# if check_winner() == 'X':
#     print('Cross wins')
#     break
# if check_winner() == '0':
#     print('Nought wins')
#     break
# if check_winner() == '*' and turn == 9:
#     print('Draw game')


#
# def print_board(board):
#     for row in board:
#         print(" | ".join(row))
#         print("-" * 5)
#
# def check_winner(board, player):
#     for row in board:
#         if all([cell == player for cell in row]):
#             return True
#     for col in range(3):
#         if all([board[row][col] == player for row in range(3)]):
#             return True
#     if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
#         return True
#     return False
#
# def tic_tac_toe():
#     board = [[" " for _ in range(3)] for _ in range(3)]
#     current_player = "X"
#     for _ in range(9):
#         print_board(board)
#         row, col = map(int, input(f"Player {current_player}, enter row and column (0, 1, or 2): ").split())
#         if board[row][col] == " ":
#             board[row][col] = current_player
#             if check_winner(board, current_player):
#                 print_board(board)
#                 print(f"Player {current_player} wins!")
#                 return
#             current_player = "O" if current_player == "X" else "X"
#         else:
#             print("Cell already taken, try again.")
#     print_board(board)
#     print("It's a draw!")
#
# if __name__ == "__main__":
#     tic_tac_toe(

def find_pairs(n):
    pairs = []
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                pairs.append((i, j))
    return pairs
def generate_password(n):
    pairs = find_pairs(n)
    password = ""
    for pair in pairs:
        password += str(pair[0]) + str(pair[1])
    return password

n = int(input("Введите число от 3 до 20: "))
result = generate_password(n)
print(f"Нужный пароль: {result}")