a = []
for _ in range(9) :
    a.append(list(map(int,input().split())))
max_val = max(map(max,a))
print(max(map(max,a)))
a = [[i+1,j+1] for i in range(9) for j in range(9) if a[i][j] == max_val]
print(*a[0])