a,b = input().split()
b = int(b)
a = a[::-1]
k=0
for i in range(len(a)):
    try:
        p = int(a[i])
        k += p * (b**(i))
    except:
        p = ord(a[i]) - 0x41 + 10
        k += p * (b**(i))
print(k)