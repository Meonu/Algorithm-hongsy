a,b = map(int,input().split())
#this Solve is 52ms
"""
k = 0
for i in range(1,a+1):
    if a%i==0:
        if k + 1 == b:
            print(i)
            exit(0)
        else:
            k+=1
print(0)
            """
#this Solve is 36ms
try:
    print([i for i in range(1,a+1) if a%i==0][b-1])
except:
    print(0)