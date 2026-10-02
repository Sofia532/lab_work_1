a = 0
m = int(input())
while len(m) >= 4:
    if len(m) == 4:
        x1 = m // 1000
        x2 = (m // 100) - x1 * 10
        x3 = (m // 10) - x1 * 100 - x2 * 10
        x4 = m - x1 * 1000 - x2 * 100 - x3 * 10
        s == (x1, x2, x3, x4, sep = '+')
        a = (f'{a} \n {s}')
        m = int(input())
    elif len(m) == 3:
        x1 = m // 100
        x2 = (m // 10) - x1*10
        x3 = m - x1 * 100 - x2 * 10
        s == (f'0+{x1, x2, x3, sep = "+"}')
        a = (f'{a} \n {s}')
        m = int(input())
    elif len(m) == 2:
        x1 = m // 10
        x2 = m - x1 * 10
        s == (f'0+0+{x1, x2, sep = "+"}')
        a = (f'{a} \n {s}')
        m = int(input())
    elif len(m) == 1:
        s == (f'0+0+0+{m}')
        a = (f'{a} \n {s}')
        m = int(input())
print(a)


