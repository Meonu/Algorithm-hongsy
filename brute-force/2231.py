n = int(input())
for i in range(0,n+1):
    if i + sum(list(map(int,str(i)))) == n:
        print(i)
        exit(0)
print(0)