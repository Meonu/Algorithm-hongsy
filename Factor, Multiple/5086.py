c = ''
while True:
    a,b = map(int,input().split())
    if a==0:
        break
    if a%b == 0:
        c += 'multiple\n'
    elif b%a == 0:
        c+= 'factor\n'
    else:
        c += 'neither\n'

print(c[:-1])