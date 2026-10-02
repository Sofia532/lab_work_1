m = ''
q = input()
w = input()
while len(m) < 23:
    a = int(input())
    if len(str(a)) == 4:
        x1 = a // 1000
        x2 = (a // 100) - x1 * 10
        x3 = (a // 10) - x1 * 100 - x2 * 10
        x4 = a - x1 * 1000 - x2 * 100 - x3 * 10
        t = f'{x1}{q}{x2}{q}{x3}{q}{x4}'
        if m == '':
            m = t
        else:
            m = m + w + t
    elif len(str(a))  == 3:
        x1 = a // 100
        x2 = (a // 10) - x1 * 10
        x3 = a - x1 * 100 - x2 * 10
        t = f'0{q}{x1}{q}{x2}{q}{x3}'
        if m == '':
            m = t
        else:
            m = m + w + t
    elif len(str(a))  == 2:
        x1 = a // 10
        x2 = a - x1 * 10
        t = f'0{q}0{q}{x1}{q}{x2}'
        m = m + w + t
    elif len(str(a)) == 1:
        t = f'0{q}0{q}0{q}{x1}'
        if m == '':
            m = t
        else:
            m = m + w + t
print(m)
