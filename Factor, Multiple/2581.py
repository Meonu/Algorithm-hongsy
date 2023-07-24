def prime_list(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우 
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

p = prime_list(10000)
m = int(input())
n = int(input())

s = [k for k in p if k>=m and k<=n]

try:
    a = s[0]
    print(sum(s))
    print(s[0])
except:
    print(-1)

