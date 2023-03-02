grid = '         '
possible_moves = [['1', '1'], ['1', '2'], ['1', '3'],
                  ['2', '1'], ['2', '2'], ['2', '3'],
                  ['3', '1'], ['3', '2'], ['3', '3']]
possible_values = [1, 2, 3]
players = ''
turn = 1
game_round = 0

print('---------')
print('|' + ' ' + grid[0] + ' ' + grid[1] + ' ' + grid[2] + ' ' + '|')
print('|' + ' ' + grid[3] + ' ' + grid[4] + ' ' + grid[5] + ' ' + '|')
print('|' + ' ' + grid[6] + ' ' + grid[7] + ' ' + grid[8] + ' ' + '|')
print('---------')


def win_x():
    global grid
    grid = ''.join(grid)
    if grid[::3] == 'XXX' or grid[3:6] == 'XXX' or grid[6::] == 'XXX':
        return True
    elif grid[2:7:2] == 'XXX' or grid[0:9:4] == 'XXX':
        return True
    elif grid[0:7:3] == 'XXX' or grid[1:8:3] == 'XXX' or grid[2:9:3] == 'XXX':
        return True


def win_o():
    global grid
    grid = ''.join(grid)
    if grid[::3] == 'OOO' or grid[3:6] == 'OOO' or grid[6::] == 'OOO':
        return True
    elif grid[2:7:2] == 'OOO' or grid[0:9:4] == 'OOO':
        return True
    elif grid[0:7:3] == 'OOO' or grid[1:8:3] == 'OOO' or grid[2:9:3] == 'OOO':
        return True


def check_digit():
    for m in move:
        if m.isdigit() is False:
            return True


def check_coord():
    for m in move:
        if int(m) not in possible_values:
            return True


def check_if_occ():
    global grid
    for i, x in enumerate(grid):
        grid = list(grid)
        if possible_moves[i] == move:
            if grid[i] != ' ':
                return True


def switch_players():
    global turn
    global players

    if turn % 2 != 0:
        players = 'X'
    else:
        players = 'O'


while True:

    move = input().split()

    if check_digit():
        print('You should enter numbers!')
    elif check_coord():
        print('Coordinates should be from 1 to 3!')
    elif check_if_occ():
        print('This cell is occupied! Choose another one!')
    else:
        if move in possible_moves:
            for i, x in enumerate(grid):
                grid = list(grid)
                if possible_moves[i] == move:
                    round += 1
                    if grid[i] == ' ':
                        switch_players()
                        turn += 1
                        grid[i] = players
                        print('---------')
                        print('|' + ' ' + grid[0] + ' ' + grid[1] + ' ' + grid[2] + ' ' + '|')
                        print('|' + ' ' + grid[3] + ' ' + grid[4] + ' ' + grid[5] + ' ' + '|')
                        print('|' + ' ' + grid[6] + ' ' + grid[7] + ' ' + grid[8] + ' ' + '|')
                        print('---------')


    if win_x():
        print('X wins')
        break
    elif win_o():
        print('O wins')
        break
    elif game_round == 9 and win_x() is None and win_o() is None:
        print('Draw')
        break

