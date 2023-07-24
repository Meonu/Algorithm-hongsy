def calc(x):
    Q = x // 25
    x -= Q * 25
    D = x // 10
    x -= D * 10
    N = x // 5
    x -= N * 5
    P = x // 1
    return [Q,D,N,P]


n = int(input())

sum = []
for _ in range(n):
    a = int(input())
    sum.append(calc(a))

for k in sum:
    print(*k)
