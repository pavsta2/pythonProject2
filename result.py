def all_moves_avail(field):   #формирвание списка всех ходов
    zero_square = 10
    all_moves = []
    for i in range(1, field+1):
        for j in range(1, field+1):
            current_square = zero_square + j
            all_moves_new = all_moves + [current_square]
            all_moves = all_moves_new
        zero_square += 10
    return all_moves

def print_field(field):   #печать поля
    zero_square = 10
    print("_______" * field)
    for i in range(1, field+1):
        for j in range(1, field+1):
            current_square = zero_square + j
            if current_square in list_pl1:
                current_square = "88"
            if current_square in list_pl2:
                current_square = "00"
            print(" ", current_square, " ", end="|")
        zero_square += 10
        print("\n", "______|" * field, sep="")

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
    if kombination_hor == field:
        winner = pl
    elif kombination_ver == field:
        winner = pl
    elif kombination_diag_1 == field:
        winner = pl
    elif kombination_diag_2 == field:
        winner = pl
    return winner

if __name__ == "__main__":

    field = int(input("Введите размер поля: "))

    list_pl1 = []
    list_pl2 = []

    all_moves = all_moves_avail(field)
    print_field(field)

    while True:

        move1 = int(input("Игрок 1, Введите ваш ход(выберите номер клетки, куда поставить крестик): "))

        while move1 not in all_moves:   #проверка возможности хода
            print_field(field)
            print("такая клетка занята или отсутствует")
            move1 = int(input("Повторите ваш ход: "))

        move = move1
        list_pl = list_pl1
        pl = 1
        if move_check(move, list_pl, pl) == 1:
            list_pl1 = list_pl1 + [move1]
            all_moves.remove(move1)
            print_field(field)
            print("Игрок 1 выиграл!")
            break

        list_pl1 = list_pl1 + [move1]
        all_moves.remove(move1)

        if not all_moves:
            list_pl1 = list_pl1 + [move1]
            print_field(field)
            print("Игра окончена. Ничья!")
            break

        print_field(field)

        move2 = int(input("Игрок 2, Введите ваш ход(выберите номер клетки, куда поставить нолик): "))

        #while isinstance(move2, int) != True:
            #all_moves_avail(field)
            #print("Вы ввели не число, введите номер клетки")
            #move2 = int(input("Повторите ваш ход: "))

        while move2 not in all_moves:
            print_field(field)
            print("такая клетка занята или отсутствует")
            move2 = int(input("Повторите ваш ход: "))

        move = move2
        list_pl = list_pl2
        pl = 2
        if move_check(move, list_pl, pl) == 2:
            list_pl2 = list_pl2 + [move2]
            all_moves.remove(move2)
            print_field(field)
            print("Игрок 2 выиграл!")
            break

        list_pl2 = list_pl2 + [move2]
        all_moves.remove(move2)

        if not all_moves:
            list_pl2 = list_pl2 + [move2]
            print_field(field)
            print("Игра окончена. Ничья!")
            break

        print_field(field)

