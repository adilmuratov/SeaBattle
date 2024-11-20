from random import randint

place = [0] * 7
taken_place = []
count_one_point_ship = 4
count_two_point_ship = 2
count_three_point_ship = 1

for i in range(len(place)):
    place[i] = ["[0]"] * 7

def generation_of_ships():
    global place
    global taken_place
    global count_one_point_ship
    global count_two_point_ship
    global count_three_point_ship

    while count_one_point_ship != 0:
        checker = 1
        ship_row = randint(0, 6)
        ship_column = randint(0, 6)

        for f in range(len(taken_place)):
            if taken_place[f][0] == ship_row and taken_place[f][1] == ship_column:
                checker = 0

        if checker == 1:
            place[ship_row][ship_column] = "[1]"
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

    while count_two_point_ship != 0:
        checker_second_point = 1
        checker = 1
        ship_row1 = randint(0, 6)
        ship_column1 = randint(0, 6)
        useful_points = [
            (ship_row1 + 1, ship_column1),
            (ship_row1, ship_column1 + 1),
            (ship_row1 - 1, ship_column1),
            (ship_row1, ship_column1 - 1)
        ]
        ship_row2 = randint(0, 6)
        ship_column2 = randint(0, 6)

        while checker_second_point != 0:
            if (ship_row2, ship_column2) in useful_points:
                checker_second_point = 0
            else:
                ship_row2 = randint(0, 6)
                ship_column2 = randint(0, 6)

        for f in range(len(taken_place)):
            if taken_place[f][0] == ship_row1 and taken_place[f][1] == ship_column1:
                checker = 0
            else:
                if taken_place[f][0] == ship_row2 and taken_place[f][1] == ship_column2:
                    checker = 0
        if checker == 1:
            place[ship_row1][ship_column1] = "[2]"
            taken_place.append([ship_row1, ship_column1])
            taken_place.append([ship_row1 - 1, ship_column1])
            taken_place.append([ship_row1 - 1, ship_column1 - 1])
            taken_place.append([ship_row1 - 1, ship_column1 + 1])
            taken_place.append([ship_row1, ship_column1 - 1])
            taken_place.append([ship_row1, ship_column1 + 1])
            taken_place.append([ship_row1 + 1, ship_column1 - 1])
            taken_place.append([ship_row1 + 1, ship_column1])
            taken_place.append([ship_row1 + 1, ship_column1 + 1])

            place[ship_row2][ship_column2] = "[2]"
            taken_place.append([ship_row2, ship_column2])
            taken_place.append([ship_row2 - 1, ship_column2])
            taken_place.append([ship_row2 - 1, ship_column2 - 1])
            taken_place.append([ship_row2 - 1, ship_column2 + 1])
            taken_place.append([ship_row2, ship_column2 - 1])
            taken_place.append([ship_row2, ship_column2 + 1])
            taken_place.append([ship_row2 + 1, ship_column2 - 1])
            taken_place.append([ship_row2 + 1, ship_column2])
            taken_place.append([ship_row2 + 1, ship_column2 + 1])

            count_two_point_ship -= 1


    while count_three_point_ship != 0:
        checker_second_point = 1
        checker = 1
        ship_row1 = randint(0, 6)
        ship_column1 = randint(0, 6)
        useful_points1 = [
            (ship_row1 + 1, ship_column1),
            (ship_row1, ship_column1 + 1),
            (ship_row1 - 1, ship_column1),
            (ship_row1, ship_column1 - 1)
        ]
        ship_row2 = randint(0, 6)
        ship_column2 = randint(0, 6)
        ship_row3 = 0
        ship_column3 = 0

        while checker_second_point != 0:
            if (ship_row2, ship_column2) in useful_points1:
                checker_second_point = 0
            else:
                ship_row2 = randint(0, 6)
                ship_column2 = randint(0, 6)

        useful_points2 = []

        if ship_row1 == ship_row2:
            if ship_column1 - ship_column2 < 0:
                useful_points2.append((ship_row1, ship_column1 - 1))
                useful_points2.append((ship_row2, ship_column2 + 1))
            else:
                useful_points2.append((ship_row2, ship_column2 - 1))
                useful_points2.append((ship_row1, ship_column1 + 1))
        elif ship_column1 == ship_column2:
            if ship_row1 - ship_row2 < 0:
                useful_points2.append((ship_row1 - 1, ship_column1))
                useful_points2.append((ship_row2 + 1, ship_column2))
            else:
                useful_points2.append((ship_row2 - 1, ship_column2))
                useful_points2.append((ship_row1 + 1, ship_column1))

        if useful_points2[0] not in taken_place and useful_points2[0][0] > 0 and useful_points2[0][1] > 0:
            ship_row3 = useful_points2[0][0]
            ship_column3 = useful_points2[0][1]
        elif useful_points2[1] not in taken_place and useful_points2[1][0] > 0 and useful_points2[1][1] > 0:
            ship_row3 = useful_points2[1][0]
            ship_column3 = useful_points2[1][1]
        else:
            continue

        for f in range(len(taken_place)):
            if taken_place[f][0] == ship_row1 and taken_place[f][1] == ship_column1:
                checker = 0
            else:
                if taken_place[f][0] == ship_row2 and taken_place[f][1] == ship_column2:
                    checker = 0
                else:
                    if taken_place[f][0] == ship_row3 and taken_place[f][1] == ship_column3:
                        checker = 0

        if checker == 1:
            place[ship_row1][ship_column1] = "[3]"
            place[ship_row2][ship_column2] = "[3]"
            place[ship_row3][ship_column3] = "[3]"

            count_three_point_ship -= 1

generation_of_ships()

for i in range(len(place)):
    result = ""
    for f in range(7):
        result += place[i][f]
    print(result)
