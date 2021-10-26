all_moves = [11, 12, 13]
move = int(input("Введите ваш ход: "))
while move not in all_moves:
    print("такая клетка занята или отсутствует")
    move = int(input("Введите ваш ход: "))






