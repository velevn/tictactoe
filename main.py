board_size = 3
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player_vs_player = '1'
player_vs_ai = '2'

# функция отрисовки поля
def draw():
    print(' ' + '_'*17)

    for i in range(board_size):
        print('|' + (' '*4 + ' |')*3)
        print('| ', board[i*3], ' | ', board[i*3+1], ' | ', board[i*3+2], ' |')
        print('|' + ('_'*5+'|')*3)


# функция хода игрока
def step_player(index, char):
    if (index < 1 or index > 10 or board[index-1] in ('X', 'O')):
        return False

    board[index-1] = char
    return True


def step_ai():
    possible_steps = [i-1 for i in board if type(i) == int]
    win_step = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    

# проверка победной комбинации
def win_check():
    win = False
    win_comb = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    for i in win_comb:
        if (board[i[0]] == board[i[1]] and board[i[1]] == board[i[2]]):
            win = board[i[0]]
    return win

# запуск игры
def start_game():
    current_player = 'X'
    ai_player = 'O'

    step = 1

    draw()

    print('')

    while (step < 10) and (win_check() == False):
        print('Ходит игрок: ' + current_player)
        index = int(input('Введите номер ячейки: '))

        if (step_player(index, current_player)):


            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'

            step += 1

            draw()
        else:
            print('Неудачная попытка!')

    if step == 10:
        print('')
        print('Ничья! Игра окончена.')
    else:
        print('')
        print('Победил игрок:' + win_check())


def main():
    start_game()


if __name__ == '__main__':
    print('')
    print('-'*4 + 'XO' + '-'*4 + 'КРЕСТИКИ-НОЛИКИ' + '-'*4 + 'XO' + '-'*4)
    print('Добро пожаловать в игру!')

    main()
