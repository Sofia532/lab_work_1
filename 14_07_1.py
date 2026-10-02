from math import sqrt as sq
a = float(input())
b = float(input())
c = float(input())
D = b ** 2 - 4 * a * c
b1 = - b
if D > 0 and a != 0 and ((b1 - sq(D)) / (2 * a)) < ((b1 + sq(D)) / (2 * a)):
    print(f'{(b1 - sq(D)) / (2 * a):.5f} {(b1 + sq(D)) / (2 * a):.5f}')
elif D > 0 and a != 0 and ((b1 - sq(D)) / (2 * a)) > ((b1 + sq(D)) / (2 * a)):
    print(f'{(b1 + sq(D)) / (2 * a):.5f} {(b1 - sq(D)) / (2 * a):.5f}')
elif D == 0 and a != 0:
    print(f'{(b1 + sq(D)) / (2 * a)}')
else:
    print('None')



