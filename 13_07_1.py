n = float(input())
m = float(input())
b = float(input())
if b < (n + m) and n < (b + m) and m < (n + m):
    print('Существует.')
else:
    print('Не существует.')
