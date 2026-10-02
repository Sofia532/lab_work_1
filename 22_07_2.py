n = input()
m = float(input())
if 'gold' in n and int(len(n)) >= m:
    print('A goldfish!')
elif 'gold' in n:
    print('Only one thing!')
elif int(len(n)) >= m:
    print('Only one thing!')
else:
    print("Either it's not a fish, or it's not a golden one.")
