place = [0] * 5

for i in range(len(place)):
    place[i] = [0] * 5

place[-1][-1] = "x"

for i in place:
    print(i)