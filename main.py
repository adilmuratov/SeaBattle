from random import randint
import os

score_list = {}
limiter = 40

def gameplay():
    global limiter
    score = 0
    place = [0] * 7
    visible_place = [0] * 7
    taken_place = []
    count_one_point_ship = 4
    count_two_point_ship = 2
    count_three_point_ship = 1

    #generation of place
    for i in range(len(place)):
        place[i] = ["[0]"] * 7
        visible_place[i] = ["[*]"] * 7
    #generation ships
    while True:
        fresher = 0
        counter = 0

        #generation one point ships
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

        #generation two points ships
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

        #generation three points ship
        while count_three_point_ship != 0:
            counter += 1
            if counter > 10000:
                fresher += 1
                break

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

        if fresher == 1:
            #print("bug")
            count_one_point_ship = 4
            count_two_point_ship = 2
            taken_place = []
            for i in range(len(place)):
                place[i] = ["[0]"] * 7
            continue

        break

    count_killed_ships = 0
    used_points = []
    coordinates_three_points_ship = []

    #for i in range(7):
    #    print(place[i])

    #game process
    while True:
        print("  1  2  3  4  5  6  7")
        for i in range(len(visible_place)):
            result = str(i + 1) + " "
            for f in range(7):
                result += visible_place[i][f]
            print(result)

        coordinates = input()

        if len(coordinates) != 3:
            os.system("cls")
            print("Please enter coordinates right")
            continue

        coordinates = coordinates.split()
        a = int(coordinates[0]) - 1
        b = int(coordinates[1]) - 1

        if (a, b) in used_points:
            os.system("cls")
            print("You also attacked this coordinates")
            continue

        if place[a][b] == "[0]":
            visible_place[a][b] = "[m]"
        elif place[a][b] == "[1]":
            visible_place[a][b] = "[d]"
            count_killed_ships += 1
        elif place[a][b] == "[2]":
            try:
                if visible_place[a - 1][b] == "[h]":
                    visible_place[a][b] = "[d]"
                    visible_place[a - 1][b] = "[d]"
                    count_killed_ships += 1
                elif visible_place[a - 1][b] == "[*]" and visible_place[a][b] == "[*]":
                    visible_place[a][b] = "[h]"
            except IndexError:
                pass
            try:
                if visible_place[a + 1][b] == "[h]":
                    visible_place[a][b] = "[d]"
                    visible_place[a + 1][b] = "[d]"
                    count_killed_ships += 1
                elif visible_place[a + 1][b] == "[*]" and visible_place[a][b] == "[*]":
                    visible_place[a][b] = "[h]"
            except IndexError:
                pass
            try:
                if visible_place[a][b + 1] == "[h]":
                    visible_place[a][b] = "[d]"
                    visible_place[a][b + 1] = "[d]"
                    count_killed_ships += 1
                elif visible_place[a][b + 1] == "[*]" and visible_place[a][b] == "[*]":
                    visible_place[a][b] = "[h]"
            except IndexError:
                pass
            try:
                if visible_place[a][b - 1] == "[h]":
                    visible_place[a][b] = "[d]"
                    visible_place[a][b - 1] = "[d]"
                    count_killed_ships += 1
                elif visible_place[a][b - 1] == "[*]" and visible_place[a][b] == "[*]":
                    visible_place[a][b] = "[h]"
            except IndexError:
                pass
        elif place[a][b] == "[3]":
            if len(coordinates_three_points_ship) != 2:
                visible_place[a][b] = "[h]"
                coordinates_three_points_ship.append((a, b))
            else:
                visible_place[a][b] = "[d]"
                visible_place[coordinates_three_points_ship[0][0]][coordinates_three_points_ship[0][1]] = "[d]"
                visible_place[coordinates_three_points_ship[1][0]][coordinates_three_points_ship[1][1]] = "[d]"
                count_killed_ships += 1


        score += 1
        used_points.append((a, b))
        os.system("cls")

        if score >= limiter or count_killed_ships == 7:
            break

    return score

while True:
    name = input("Enter your name:")
    os.system("cls")
    score = gameplay()
    score_list[name] = score
    answer = None
    if score == 40:
        print("You lost, you will try again?")
        answer = input("Yes or No:")
    else:
        print("You wined! You will play again?")
        answer = input("Yes or No:")
    os.system("cls")
    while answer != "Yes" and answer != "No":
        answer = input("Please, enter correct Yes or No:")
    os.system("cls")
    if answer == "No":
        break

sorted_score_list = sorted(score_list.items(), key=lambda item: item[1])

for i in range(len(sorted_score_list)):
    print(str(i) + ")", sorted_score_list[i][0] + ": " + str(sorted_score_list[i][1]))
