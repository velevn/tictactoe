# Игра Крестики-нолики.

board_size = 3  # размер игрового поля

board = [1, 2, 3, 4, 5, 6, 7, 8, 9] #количество клеток игрового поля


# Вывод игрового поля
def draw():
    print(''+'_' * 5 * board_size)
    for i in range(board_size):
        print('|'+((' ' * 4 + '|') * 3))
        print('|', board[i*3], ' |', board[i*3+1], ' |', board[i*3+2], ' |')
        print('|'+(('_' * 4+'|') * 3))


# Функция отвечающая за ход игрока
def step_game(index, char):
    if (index > 10 or index < 1 or board[index-1] in ('X', 'O')):
        return False

    board[index-1] = char
    return True


# Проверка победной комбинации
def check_win():
    win = False
    win_situation = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                     (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    for pos in win_situation:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]):
            win = board[pos[0]]
    return win


# Запуск
def game_start():
    print('Игра Крестики-нолики.')

    current_player = 'X'  # текущий игрок
    step = 1  # номер хода

    draw()

    while (step < 10) and (check_win() == False):
        index = input('Ходит игрок. ' + current_player +
                      '\nВведите номер поля:')

        if (step_game(int(index), current_player)):
            print('Ход сделан.')

            # меняем игрока
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'

            step += 1

            draw()
        else:
            print('Неудачная попытка. Повторите ход.')

    if (step == 10):
        print('Ничья. Игра окончена!')
    else:
        print('Выиграл ' + check_win())


game_start()
