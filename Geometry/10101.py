a = []
for i in range(3):
    a.append(int(input()))
if sum(a) != 180:
    print('Error')
    exit()
else:
    if a.count(60) == 3:
        print('Equilateral')
        exit()
    for i in range(3):
        if a.count(a[i]) == 2:
            print('Isosceles')
            exit()
print('Scalene')