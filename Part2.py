count = 0
lights_number = 0
scad = 0
adun = 0
stins = 1000000
aprins = 0
toggle = 0
lights_number = 0
matrix1 = []
for i in range(1000):
    row = []
    for j in range(1000):
        row.append(0)
    matrix1.append(row)

with open('coding_challenge_input.txt') as file:
    while True:
        line = file.readline()
        if not line:
            break
        if 'toggle' in line:
            x = line.split()
            coord1 = x[1].split(',')
            coord2 = x[3].split(',')

            a1_toggle = int(coord1[0])
            b1_toggle = int(coord1[1])

            a2_toggle = int(coord2[0])
            b2_toggle = int(coord2[1])

            for i in range(a1_toggle, a2_toggle + 1):
                for j in range(b1_toggle, b2_toggle + 1):
                    matrix1[i][j] += 2
        elif 'turn on' in line:
            x = line.split()
            coord1 = x[2].split(',')
            coord2 = x[4].split(',')

            a1_turnon = int(coord1[0])
            b1_turnon = int(coord1[1])

            a2_turnon = int(coord2[0])
            b2_turnon = int(coord2[1])

            for i in range(a1_turnon, a2_turnon + 1):
                for j in range(b1_turnon, b2_turnon + 1):
                    matrix1[i][j] += 1
        elif 'turn off' in line:
            x = line.split()
            coord1 = x[2].split(',')
            coord2 = x[4].split(',')

            a1_turnoff = int(coord1[0])
            b1_turnoff = int(coord1[1])

            a2_turnoff = int(coord2[0])
            b2_turnoff = int(coord2[1])

            lights_number += 1
            for i in range(a1_turnoff, a2_turnoff + 1):
                for j in range(b1_turnoff, b2_turnoff + 1):
                    if matrix1[i][j] >= 1:
                        matrix1[i][j] -= 1

for i in range(1000):
    for j in range(1000):
        lights_number = lights_number + matrix1[i][j]

print(f"Number of lights for Part2: {lights_number}")
