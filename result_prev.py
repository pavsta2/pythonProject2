def all_moves_avail(FIELD):   #формирвание списка всех ходов
    zero_square = 10
    all_moves = []
    for i in range(1, FIELD+1):
        for j in range(1, FIELD+1):
            current_square = zero_square + j
            all_moves_new = all_moves + [current_square]
            all_moves = all_moves_new
        zero_square += 10
    return all_moves

def print_field(FIELD):   #печать поля
    zero_square = 10
    print("_______" * FIELD)
    for i in range(1, FIELD+1):
        for j in range(1, FIELD+1):
            current_square = zero_square + j
            if current_square in list_pl1:
                current_square = "01"
            if current_square in list_pl2:
                current_square = "00"
            print(" ", current_square, " ", end="|")
        zero_square += 10
        print("\n", "______|" * FIELD, sep="")

def move_check_hor(move, list_pl):   #проверка комбинуии по горизонтали
    kombination_hor = 1
    i = 1
    j = 1
    while move + i in list_pl:
        kombination_hor += 1
        i = i + 1
    while move - j in list_pl:
        kombination_hor += 1
        j = j + 1
    return kombination_hor

def move_check_ver(move, list_pl):   #проверка комбинуии по вертикали
    kombination_ver = 1
    i = 10
    j = 10
    while move + i in list_pl:
        kombination_ver += 1
        i = i + 10
    while move - j in list_pl:
        kombination_ver += 1
        j = j + 10
    return kombination_ver

def move_check_diag_1(move, list_pl): #проверка комбинуии по диаг 1
    kombination_diag_1 = 1
    i = 9
    j = 9
    while move + i in list_pl:
        kombination_diag_1 += 1
        i = i + 9
    while move - j in list_pl:
        kombination_diag_1 += 1
        j = j + 9
    return kombination_diag_1

def move_check_diag_2(move, list_pl): #проверка комбинуии по диаг 2
    kombination_diag_2 = 1
    i = 11
    j = 11
    while move + i in list_pl:
        kombination_diag_2 += 1
        i = i + 11
    while move - j in list_pl:
        kombination_diag_2 += 1
        j = j + 11
    return kombination_diag_2


def move_check(move, list_pl, pl):   #проверка всех комбинаций
    winner = 0
    kombination_hor = move_check_hor(move, list_pl)
    kombination_ver = move_check_ver(move, list_pl)
    kombination_diag_1 = move_check_diag_1(move, list_pl)
    kombination_diag_2 = move_check_diag_2(move, list_pl)
    if kombination_hor == FIELD:
        winner = pl
    elif kombination_ver == FIELD:
        winner = pl
    elif kombination_diag_1 == FIELD:
        winner = pl
    elif kombination_diag_2 == FIELD:
        winner = pl
    return winner

def get_field_size():
    while True:
        try:
           FIELD = int(input("Введите размер поля"))
        except ValueError:
           print("Введите размер поля еще раз")
        else:
            return FIELD

    while True:
        FIELD = input("Введите размер поля")
        if not str(FIELD).isdigit():
            print("Введите размер поля еще раз")
        else:
            return int(FIELD)

def get_plr_step(help_text: str):
    move = int(input(help_text))
    if not str(move).isdigit():
        print(help_text)
    else:
        while move not in all_moves:  # проверка возможности хода
            print_field(FIELD)
            print("такая клетка занята или отсутствует")
            move = int(input(help_text))
        return move

def win_check(move, list_pl, pl):
    if move_check(move, list_pl, pl) == pl:
        list_pl = list_pl + [move]
        all_moves.remove(move)
        print_field(FIELD)
        print(f"Игрок {pl} выиграл!")
    else:
        list_pl = list_pl + [move]
        all_moves.remove(move)
    return move_check(move, list_pl, pl), list_pl, all_moves


if __name__ == "__main__":

    FIELD = get_field_size()

    #dict_list_pl = {  # todo dict, чтобы убрать списки list_pl1 и list_pl2
       # 1: [],
       # 2: []
    #}

    list_pl1 = []
    list_pl2 = []

    all_moves = all_moves_avail(FIELD)
    print_field(FIELD)

    while True:

        move = get_plr_step("Игрок 1, Введите ваш ход(выберите номер клетки, крестик - это 01): ")

        list_pl = list_pl1
        pl = 1
        win_check(move, list_pl, pl)
        if move_check(move, list_pl, pl) == pl:
            break
        else:
            list_pl1 = list_pl1 + [move]

        if not all_moves:
            print_field(FIELD)
            print("Игра окончена. Ничья!")
            break

        print_field(FIELD)

        move = get_plr_step("Игрок 2, Введите ваш ход(выберите номер клетки, нолик - это 00): ")

        list_pl = list_pl2
        pl = 2
        win_check(move, list_pl, pl)
        if move_check(move, list_pl, pl) == pl:
            break
        else:
            list_pl2 = list_pl2 + [move]

        if not all_moves:
            list_pl2 = list_pl2 + [move]
            print_field(FIELD)
            print("Игра окончена. Ничья!")
            break

        print_field(FIELD)

