n = int(input())
a = []
b = []
for i in range(n):
    buf = list(map(int, input().split()))
    a.append(buf[0])
    b.append(buf[1])
print((max(a)-min(a))*(max(b)-min(b)))