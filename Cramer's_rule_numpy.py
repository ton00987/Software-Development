import numpy as np
import string
import copy

var = int(input('Unknown variables: '))
matrix_A = [[] for i in range(var)]

det_A = []

for i in range(var):
    for j in range(var+1):
        matrix_A[i].append(int(input(string.ascii_lowercase[j] + str(i) + ': ')))

print()
print('Matrix')

for i in range(var):
    for j in range(var+1):
        print('{:4}'.format(matrix_A[i][j]), end='')
    print()

det_A = copy.deepcopy(matrix_A)

for i in range(var):
    del det_A[i][-1]

print()
print('Det')

for i in range(var):
    for j in range(var):
        print('{:4}'.format(det_A[i][j]), end='')
    print()

main_det = np.linalg.det(det_A)
print('Det =', main_det)

all_det = []

for i in range(var):
    # Change column to answer column
    for j in range(var):
        det_A[j][i] = matrix_A[j][var]

    print()
    print('Det_x' + str(i+1))

    for k in range(var):
        for l in range(var):
            print('{:4}'.format(det_A[k][l]), end='')
        print()

    print('Det_x' + str(i+1) + ' =', np.linalg.det(det_A))
    all_det.append(np.linalg.det(det_A))

    # Turn column back
    for j in range(var):
        det_A[j][i] = matrix_A[j][i]

print()

for i in range(var):
    print('x' + str(i+1) + ' =', all_det[i]/main_det)