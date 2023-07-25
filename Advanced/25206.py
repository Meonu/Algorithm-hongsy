grade = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}
g = 0
s = 0
for _ in range(20):
    a = input().split()
    try:
        g += float(a[1]) * grade[a[2]]
        s += float(a[1])
    except(KeyError):
        pass

print(g/s)