"""def square_point(x):
    return [[x[0],x[1]],[x[0]+10,x[1]],[x[0]+10,x[1]+10],[x[0],x[1]+10]]

def find_intersection(a,b) :
    if ((abs(a[0][0] - b[0][0]) < 10) and (abs(a[0][1] - b[0][1]) < 10)) : 
        if a[0][0] > b[0][0] : 
            tmp = a
            a = b
            b = tmp
        x = b[0][0]
        x_len = a[1][0] - b[0][0]

        if a[0][1] > b[0][1]:
            tmp = a
            a = b
            b = tmp
        y = b[0][1]
        y_len = a[2][1] - b[0][1]
        return [x,y,x_len,y_len]
    return None



print(find_intersection())"""
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