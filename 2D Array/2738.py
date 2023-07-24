import numpy as np
n,m = input().split()
a = []
b = []
for i in range(int(n)):
    a.append(input().split())

for i in range(int(n)):
    b.append(input().split())

a = np.array(a,dtype=int)
b = np.array(b,dtype=int)

sum = str(a+b)
print(sum.replace('[','').replace(']',''))