n,m = map(int,input().split())
k = list(map(int,(input().split())))
a = []
for i in range(n):
    for j in range(i+1,n):
        for p in range(j+1,n):
            if k[i]+k[j]+k[p] <= m:
                a.append(k[i]+k[j]+k[p])

m = [abs(x-m) for x in a]

print(a[m.index(min(m))])