from random import randint

place = [0] * 7
taken_place = []
count_one_point_ship = 4

for i in range(len(place)):
    place[i] = ["[0]"] * 7

checker = 1
while count_one_point_ship != 0:
    ship_row = randint(0, 6)
    ship_column = randint(0, 6)
    for f in range(len(taken_place)):
        if taken_place[f][0] == ship_row and taken_place[f][1] == ship_column:
            checker = 0
    if checker == 1:
        place[ship_row][ship_column] = "[*]"
        taken_place.append([ship_row, ship_column])
        taken_place.append([ship_row - 1, ship_column])
        taken_place.append([ship_row - 1, ship_column - 1])
        taken_place.append([ship_row - 1, ship_column + 1])
        taken_place.append([ship_row, ship_column - 1])
        taken_place.append([ship_row, ship_column + 1])
        taken_place.append([ship_row + 1, ship_column - 1])
        taken_place.append([ship_row + 1, ship_column])
        taken_place.append([ship_row + 1, ship_column + 1])
        count_one_point_ship -= 1


for i in range(len(place)):
    result = ""
    for f in range(7):
        result += place[i][f]
    print(result)

