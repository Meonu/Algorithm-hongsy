a,b = map(int,input().split())
c = ''
while a > 0:
    div = a % b
    if div < 10:
        c += str(div)
    else:
        c += chr(div - 10 + 0x41)
    a//=b
print(c[::-1])