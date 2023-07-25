import sys
a = []
b = []
for _ in range(3):
    buf = sys.stdin.readline().split()
    a.append(int(buf[0]))
    b.append(int(buf[1]))
x,y=0,0
for i in range(3):
    if a.count(a[i]) == 1:
        x = a[i]
    if b.count(b[i]) == 1:
        y = b[i]
print(f'{x} {y}')