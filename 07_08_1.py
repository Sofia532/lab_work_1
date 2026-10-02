m = ''
a = input()
while a != 'СТОП':
    m = m + (f'{a}\t{len(a)} \n') 
    a = input()
print(m)

