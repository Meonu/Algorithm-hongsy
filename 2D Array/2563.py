def color(a, x):
    for i in range(10):
        for j in range(10):
            a[x[0] + i][x[1] + j] = 1
    return a

a = [[0 for _ in range(101)] for _ in range(101) ]

n = int(input())
for _ in range(n):
    p = list(map(int,input().split()))
    a = color(a,p)

print(sum(sum(a,[])))