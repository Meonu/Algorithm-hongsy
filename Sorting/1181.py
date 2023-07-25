n = int(input())
a = [[] for _ in range(51)]
for _ in range(n):
    buf = input()
    a[len(buf)].append(buf)

for i in a:
    i = list(set(i))
    i.sort()
    for k in i:
        print(k)