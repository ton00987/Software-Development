from fractions import Fraction
import string

var = int(input('Unknown variables: '))
matrix_A = [[] for i in range(var)]

# Input Matrix
for i in range(var):
    for j in range(var+1):
        matrix_A[i].append(int(input(string.ascii_lowercase[j] + str(i) + ': ')))

a = var
first_zero = True
m = 0
while first_zero:
    if matrix_A[0][0] == 0:
        matrix_A[m], matrix_A[m+1] = matrix_A[m+1], matrix_A[m]
    else:
        first_zero = False
    m += 1
    if m == var-1:
        break

for i in range(var):
    c = matrix_A[i][i]

    # Division row with first array
    for j in range(var+1):
        matrix_A[i][j] = Fraction(matrix_A[i][j], c)

    print()
    print('Division')
    for k in range(var):
        for l in range(var + 1):
            print('{:6}'.format(str(matrix_A[k][l])), end='')
        print()

    if i == var-1:
        break

    a -= 1

    # Subtraction row with above row
    for h in range(a):
        d = matrix_A[-1-h][i]

        for g in range(var+1):
            matrix_A[-1-h][g] = (Fraction(str(d * matrix_A[i][g]))) - matrix_A[-1-h][g]

    print()
    print('Subtraction')
    for k in range(var):
        for l in range(var + 1):
            print('{:6}'.format(str(matrix_A[k][l])), end='')
        print()



all_ans = []
all_ans.append(matrix_A[-1][-1])

def cal_var(all_ans):
    ''' Calculate array '''
    num = len(all_ans)

    if num == var:
        return

    result = 0

    for f in range(num):
        result += (Fraction(all_ans[f]*matrix_A[var-num-1][-2-f]))

    ans = Fraction(matrix_A[var-num-1][-1]) - result
    all_ans.append(ans)
    cal_var(all_ans)

cal_var(all_ans)

print()

for i in range(var):
    print('x' + str(i+1) + ' =', all_ans[-1-i])