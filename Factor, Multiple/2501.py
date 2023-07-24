a,b = map(int,input().split())
k = 0

for i in range(1,a+1):
    if a%i==0:
        if k + 1 == b:
            print(i)
            exit(0)
        else:
            k+=1
            
print(0)