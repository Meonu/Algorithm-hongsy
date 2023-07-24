import numpy as np
n,m = input().split()
a = []
b = []
for i in range(int(n)):
    a.append(list(map(int, input().split())))

for i in range(int(n)):
    b.append(list(map(int, input().split())))

for i in range(0, int(n)):
    for j in range(0, int(m)):
        print(a[i][j] + b[i][j],end=' ')
    print()