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

# done формирование и отрисовка поля разделены

def print_field(FIELD):   #печать поля
    zero_square = 10
    print("_______" * FIELD)
    for i in range(1, FIELD+1):
        for j in range(1, FIELD+1):
            current_square = zero_square + j
            if current_square in dict_list_pl[1]:
                current_square = "01"   # это обозначает крестик (fixed)
            if current_square in dict_list_pl[2]:
                current_square = "00"   # это обозначает нолик (fixed)
            print(" ", current_square, " ", end="|")
        zero_square += 10
        print("\n", "______|" * FIELD, sep="")

def move_check_hor(move, dict_list_pl):   #проверка комбинуии по горизонтали
    kombination_hor = 1
    i = 1
    j = 1
    while move + i in dict_list_pl:
        kombination_hor += 1
        i = i + 1
    while move - j in dict_list_pl:
        kombination_hor += 1
        j = j + 1
    return kombination_hor

def move_check_ver(move, dict_list_pl):   #проверка комбинуии по вертикали
    kombination_ver = 1
    i = 10
    j = 10
    while move + i in dict_list_pl:
        kombination_ver += 1
        i = i + 10
    while move - j in dict_list_pl:
        kombination_ver += 1
        j = j + 10
    return kombination_ver

def move_check_diag_1(move, dict_list_pl): #проверка комбинуии по диаг 1
    kombination_diag_1 = 1
    i = 9
    j = 9
    while move + i in dict_list_pl:
        kombination_diag_1 += 1
        i = i + 9
    while move - j in dict_list_pl:
        kombination_diag_1 += 1
        j = j + 9
    return kombination_diag_1

def move_check_diag_2(move, dict_list_pl): #проверка комбинуии по диаг 2
    kombination_diag_2 = 1
    i = 11
    j = 11
    while move + i in dict_list_pl:
        kombination_diag_2 += 1
        i = i + 11
    while move - j in dict_list_pl:
        kombination_diag_2 += 1
        j = j + 11
    return kombination_diag_2


def move_check(move, dict_list_pl, pl):   #проверка всех комбинаций
    winner = 0
    kombination_hor = move_check_hor(move, dict_list_pl)
    kombination_ver = move_check_ver(move, dict_list_pl)
    kombination_diag_1 = move_check_diag_1(move, dict_list_pl)
    kombination_diag_2 = move_check_diag_2(move, dict_list_pl)
    if kombination_hor == FIELD:
        winner = pl
    elif kombination_ver == FIELD:
        winner = pl
    elif kombination_diag_1 == FIELD:
        winner = pl
    elif kombination_diag_2 == FIELD:
        winner = pl
    return winner

def get_field_size():         #запрос размера поля и проверка ошибки ввода
    while True:
        try:
           FIELD = int(input("Введите размер поля"))
        except ValueError:
           print("ошибка ввода")
        else:
            return FIELD


def get_plr_step(help_text: str):      ##запрос хода и проверка ошибки ввода

    while True:
        try:
           move = int(input(help_text))
        except ValueError:
           print("ошибка ввода")
        else:
            break

    while move not in all_moves:  # проверка возможности хода
        print_field(FIELD)
        print("такая клетка занята или отсутствует")
        move = int(input(help_text))

    return move

#def rec_plr_step(move, list_pl, pl):     #запись хода игрока без выигрыша вариант двух списков
 #   list_pl = list_pl + [move]
  #  all_moves.remove(move)
   # return list_pl

def rec_plr_step(move, dict_list_pl):     # DONE запись хода игрока без выигрыша вариант словарей
    dict_list_pl += [move]
    all_moves.remove(move)
    return dict_list_pl


if __name__ == "__main__":

    FIELD = get_field_size()

    dict_list_pl = {  # done новый вариант со словарем
       1: [],
       2: []
    }

    #list_pl1 = []   #  старый вариант со списками
    #list_pl2 = []

    all_moves = all_moves_avail(FIELD)
    print_field(FIELD)

    while True:

        #list_pl = list_pl1   # старый вариант со списками
        pl = 1

        move = get_plr_step(f"Игрок {pl}, Введите ваш ход(выберите номер клетки, крестик - это 01): ")

        dict_list_pl[pl] = rec_plr_step(move, dict_list_pl[pl])
        if move_check(move, dict_list_pl[pl], pl) == pl:   #этот блок не смог вынести в функ,т.к. содерж break глоб цикла while
            print(f"Игрок {pl} выиграл!")
            #list_pl1 = list_pl1 + [move]   # старый вариант со списками ??? append почему то не работал
            dict_list_pl[pl] += [move]
            print_field(FIELD)
            break

        if not all_moves:
            print_field(FIELD)
            print("Игра окончена. Ничья!")
            break

        print_field(FIELD)

        #list_pl = list_pl2   # старый вариант со списками
        pl = 2

        move = get_plr_step(f"Игрок {pl}, Введите ваш ход(выберите номер клетки, нолик - это 00): ")

        dict_list_pl[pl] = rec_plr_step(move, dict_list_pl[pl])
        if move_check(move, dict_list_pl[pl], pl) == pl:
            print(f"Игрок {pl} выиграл!")
            #list_pl2 = list_pl2 + [move]   # старый вариант со списками ??? append почему то не работал
            dict_list_pl[pl] += [move]
            print_field(FIELD)
            break

        if not all_moves:
            #list_pl2 = list_pl2 + [move]   # старый вариант со списками ??? append почему то не работал
            print_field(FIELD)
            print("Игра окончена. Ничья!")
            break

        print_field(FIELD)

