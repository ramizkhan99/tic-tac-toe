import os
import random

n = int(input("Enter the side length: "))

board = []
icons = ['X', 'O']
available_positions = []

def generate_board():
    for _a in range(n):
        new = []
        for _b in range(n):
            new.append('_')
            available_positions.append(str(_a) + ' ' + str(_b))
        board.append(new)

def display_board():
    print(len(str(n)) * ' ', end='\t')
    for i in range(n):
        print('\033[33m' + str(i) + '\033[0m', end=' ')
    print('\n')
    for i in range(n):
        for j in range(n):
            char = board[i][j]
            if char == 'X':
                char = '\033[32m' + char + '\033[0m'
            elif char == 'O':
                char = '\033[31m' + char + '\033[0m'
            if j == 0:
                char = '\033[33m' + str(i) + '\033[0m' + '\t' + char
            print(char, end=' ')
        print('\n')

def check_horizontal():
    flag = True
    for row in board:
        char = row[0]
        if char == '_':
            flag = False
            continue
        for i in row:
            flag = True
            if i != char:
                flag = False
                break
        if flag:
            break
    return flag

def check_vertical():
    flag = False
    for i in range(n):
        if board[0][i] != '_':
            flag = True
            for j in range(n):
                if board[j][i] != board[0][i]:
                    flag = False
                    break
            if not flag:
                continue
            else:
                break
    return flag
    
def check_diagonal():
    flag = True
    for i in range(n):
        if board[i][i] != board[0][0] or board[0][0] == '_':
            flag = False
            break
    if not flag:
        flag = True
        for i in range(n):
            if board[i][n - i - 1] != board[0][n - 1] or board[0][n - 1] == '_':
                flag = False
                break
    return flag

def check_board():
    return (check_horizontal() or check_vertical() or check_diagonal())

def check_draw():
    count = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == '_':
                count += 1
                break

    if count == 0:
        return True
    return False

def generate_ai_position():
    return random.choice(available_positions)

def main():
    clear_call = 'cls' if os.name == 'nt' else 'clear'
    game_over = False
    generate_board()
    index = int(input('You want to go first or second? (1 or 2) ')) - 1
    while not game_over:
        os.system(clear_call)
        display_board()
        char = icons[index]
        if index == 0:
            position = input('Enter position for next ' + char + ': \033[34m')
        else:
            # position = input('Enter position for next ' + char + ': \033[34m')
            position = generate_ai_position()
        index = 1 - index
        print('\033[0m')
        x = int(position.split(' ')[0])
        y = int(position.split(' ')[1])
        if board[x][y] == '_':
            available_positions.remove(str(x) + ' ' + str(y))
            board[x][y] = char
        else:
            print('Invalid board position(Position occupied)')
        if check_draw():
            game_over = True
        else:
            game_over = check_board()
            

    os.system(clear_call)
    if check_draw():
        print('Game Draw!!')
    else:
        print(icons[1 - index] + ' has won the game')
    display_board()


main()