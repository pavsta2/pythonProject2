move = int(input())
list_plyr1_moves = [11, 13]
def ply_1_move(move):
    prev_move_1_hor = move + 1
    prev_move_2_hor = move - 1
    prev_move_3_hor = move + 2
    prev_move_4_hor = move - 2
    prev_move_1_ver = move + 10
    prev_move_2_ver = move - 10
    prev_move_3_ver = move + 20
    prev_move_4_ver = move - 20
    prev_move_1_dia_1 = move + 9
    prev_move_2_dia_1 = move - 9
    prev_move_3_dia_1 = move + 18
    prev_move_4_dia_1 = move - 18
    prev_move_1_dia_2 = move + 11
    prev_move_2_dia_2 = move - 11
    prev_move_3_dia_2 = move + 22
    prev_move_4_dia_2 = move - 22

    if prev_move_1_hor in list_plyr1_moves and prev_move_2_hor in list_plyr1_moves:
        result = 1
    elif prev_move_1_hor in list_plyr1_moves and prev_move_3_hor in list_plyr1_moves:
        result = 2
    elif prev_move_2_hor in list_plyr1_moves and prev_move_4_hor in list_plyr1_moves:
        result = 3
    elif prev_move_1_ver in list_plyr1_moves and prev_move_2_ver in list_plyr1_moves:
        result = 4
    elif prev_move_1_ver in list_plyr1_moves and prev_move_3_ver in list_plyr1_moves:
        result = 5
    elif prev_move_2_ver in list_plyr1_moves and prev_move_4_ver in list_plyr1_moves:
        result = 6
    elif prev_move_1_dia_1 in list_plyr1_moves and prev_move_2_dia_1 in list_plyr1_moves:
        result = 7
    elif prev_move_1_dia_1 in list_plyr1_moves and prev_move_3_dia_1 in list_plyr1_moves:
        result = 8
    elif prev_move_2_dia_1 in list_plyr1_moves and prev_move_4_dia_1 in list_plyr1_moves:
        result = 9
    elif prev_move_1_dia_2 in list_plyr1_moves and prev_move_2_dia_2 in list_plyr1_moves:
        result = 10
    elif prev_move_1_dia_2 in list_plyr1_moves and prev_move_3_dia_2 in list_plyr1_moves:
        result = 11
    elif prev_move_2_dia_2 in list_plyr1_moves and prev_move_4_dia_2 in list_plyr1_moves:
        result = 12
    else:
        result = 0
    return result
print(ply_1_move(move))
print(11 and 13 and 5 in list_plyr1_moves)

if ply_1_move(move) > 0:
    print("выигрыш")