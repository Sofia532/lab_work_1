from math import ceil as c
n = int(input())
i = int(input())
a = n * i
s = c(a / 8)
d = s // 1024
f = s - (d * 1024)
if s < 1024:
    print(f'{s} байт')
elif f == 0:
    print(f'{d} Кбайт') 
else:
    print(f'{d} Кбайт и {f} байт')
#  a - колличество бит(всего)
#  s - колличество байт(всего)
#  d - колличество Кбайт(всего)
#  8 бит = 1 байт  1 кб = 1024 байт
