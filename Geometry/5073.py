s = ['', 'Equilateral','Isosceles','Scalene']
while True:
    a = list(map(int,input().split()))
    if a[0] == 0:
        break
    a.sort()
    if a[2] >= a[1] + a[0]:
        print('Invalid')
        continue
    a = list(set(a))
    print(s[len(a)])
    