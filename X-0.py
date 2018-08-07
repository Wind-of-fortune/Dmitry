import random

def to_the_end(board):
    k = 0 
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j - 2] == board[i][j - 1] == board[i][j] != '-':
                return print('Игра завершена','игрок1 за',board[i][j-1],'победил'), False

            if board[i - 2][j] == board[i - 1][j] == board[i][j] != '-':
                return print('Игра завершена','игрок2 за',board[i-1][j],'победил'), False

            if board[0][0] == board[1][1] == board[2][2] != '-':
                return print('Игра завершена','игрок3 за',board[1][1],'победил'), False

            if board[2][0] == board[1][1] == board[0][2] != '-':
                return print('Игра завершена','игрок4 за',board[1][1],'победил'), False
            if board[i][j] == '-':
                k = k+1

    if k == 0:
        return print('Ничья!')
    return True

def move_func(move,board,x_o,comp_x_o):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if move == 1:
                if board[2][0] == '-':
                    board [2][0] = x_o
                    return board
                else:
                    return print('Не вставайте на чужое поле'), None
            if move == 2:
                if board[2][1] == '-':
                    board [2][1] = x_o
                    return board
                else:
                    return print('Не вставайте на чужое поле'), None
            if move == 3:
                if board[2][2] == '-':
                    board [2][2] = x_o
                    return board
                else:
                    return print('Не вставайте на чужое поле'), None
            if move == 4:
                if board[1][0] == '-':
                    board [1][0] = x_o
                    return board
                else:
                    return print('Не вставайте на чужое поле'), None
            if move == 5:
                if board[1][1] == '-':
                    board [1][1] = x_o
                    return board
                else:
                    return print('Не вставайте на чужое поле'), None
            if move == 6:
                if board[1][2] == '-':
                    board [1][2] = x_o
                    return board
                else:
                    return print('Не вставайте на чужое поле'), None
            if move == 7:
                if board[0][0] == '-':
                    board [0][0] = x_o
                    return board
                else:
                    return print('Не вставайте на чужое поле'), None
            if move == 8:
                if board[0][1] == '-':
                    board [0][1] = x_o
                    return board
                else:
                    return print('Не вставайте на чужое поле'), None
            if move == 9:
                if board[0][2] == '-':
                    board [0][2] = x_o
                    return board
                else:
                    return print('Не вставайте на чужое поле'), None
    return board

def move_comp(board,x_o):
    if board[0][0] == board[0][1] == x_o:
        if board[0][2] == '-':
            board[0][2] = comp_x_o
            return board
    if board[1][0] == board[1][1] == x_o:
        if board[1][2] == '-':
            board[1][2] = comp_x_o
            return board
    if board[2][0] == board[2][1] == x_o:
        if board[2][2] != '-':
            board[2][2] = comp_x_o
            return board
    if board[0][0] == board[1][0] == x_o:
        if board[2][0] != '-':
            board[2][0] = comp_x_o
            return board
    if board[0][1] == board[1][1] == x_o:
        if board[2][1] != '-':
            board[2][1] = comp_x_o
            return board
    if board[0][2] == board[1][2] == x_o:
        if board[2][2] != '-':
            board[2][2] = comp_x_o
            return board
    if random.randint(0,10) >= 7:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '-':
                    board[i][j] = comp_x_o
                    return board
    if random.randint(0,10) <= 3:
        for i in range(1, len(board)):
            for j in range(2, len(board[i])):
                if board[i][j] == '-':
                    board[i][j] = comp_x_o
                    return board
    else:
        for i in range(2, len(board)):
            for j in range(1, len(board[i])):
                if board[i][j] == '-':
                    board[i][j] = comp_x_o
                    return board

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '-':
                board[i][j] = comp_x_o
                return board

    return print('hi')

print('Вас преведствует игра X-0, именуемая также крестики-нолики, начинаем!!!')
print()
n = 3
s = 0

x_o = str(input(('Введите за X или за 0 вы будете играть: ')))

if x_o != '0':
    comp_x_o = '0'
else:
    comp_x_o = 'X'


print('если вы выбрали поле кратное трем то управление будет осуществляться с помощью дом клавиатуры - num Lock')
print('5 - это центр поля')
print('для поля не кратного 3м вам нужно будет вводить число - порядковый элемент массива, там где вы хотите поставить крестик')

priority = int(input('Кто делает первый ход?\n 1 - Вы, 0 -Компьютер\n  '))

board = [['-' for i in range(n)] for j in range(n)]

for i in range(len(board)):
    print(*board[i])


if priority == True:
    while to_the_end(board) == True:

        move = int(input('Делайте ход !  \n'))

        if move_func(move, board, x_o, comp_x_o) == (None, None):
            move = int(input('Делайте ход !  \n'))
            move_func(move, board, x_o, comp_x_o)

        for i in range(len(board)):
            print(*board[i])
        print()

        if to_the_end(board) == True:
            move_comp(board,x_o)
            for i in range(len(board)):
                print(*board[i])
            print()
        else:
            break
else:
    while to_the_end(board) == True:
        s += 1
        print()
        if s == 1:
            if random.randint(0,10) < 8:
                board[1][1] = comp_x_o
                for i in range(len(board)):
                    print(*board[i])
                print()
            else:
                print()
                move_comp(board,x_o)
                for i in range(len(board)):
                    print(*board[i])
                print()
        else:
            print()
            move_comp(board,x_o)
            for i in range(len(board)):
                print(*board[i])
            print()

        if to_the_end(board) == True:

            move = int(input('Делайте ход !  \n'))

            if move_func(move, board, x_o, comp_x_o) == (None, None):
                move = int(input('Делайте ход !  \n'))
                move_func(move, board, x_o, comp_x_o)

            for i in range(len(board)):
                print(*board[i])
            print()
        else:
            break














