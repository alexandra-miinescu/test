count = 0
lights_number = 0
scad = 0
adun = 0
matrix1 = []
for i in range(1000):
    row = []
    for j in range(1000):
        row.append('ON')
    matrix1.append(row)

for i in range(499, 501):
    for j in range(499, 501):
        count += 1
        matrix1[i][j] = 'OFF'

lights_on = 1000000 - count

for i in range(0, 1000):
    for j in range(499, 501):
        if matrix1[i][j] == 'OFF':
            count -= 1
            scad += 1
            matrix1[i][j] = 'Toggle'
        elif matrix1[i][j] == 'ON':
            count += 1
            adun += 1  #we start from level 0, so we add 1 if the light is on
            matrix1[i][j] = 'Toggle'

lights_on = 1000000 - count

print(lights_on)

for i in range(1000):
    for j in range(1000):
        if matrix1[i][j] == 'ON':
            lights_number += 1
        elif matrix1[i][j] == 'OFF':
            lights_number -= 1
        else:
            lights_number += 2

lights_number = lights_number + adun

print(lights_number)
