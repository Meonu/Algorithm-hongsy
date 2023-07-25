n = int(input())
i = 2
### 이 코드는 너무 오래걸림
while n != 1:
    while n % i ==0:
        print(i)
        n = n // i
    i += 1

###소수 찻을때는 반복을 sqrt까지만 하자
n = int(input())
i = 2
t = n
while n >= i*i:
    while t % i == 0:
        print(i)
        t /= i
    i+=1

if t != 1:
    print(int(t))