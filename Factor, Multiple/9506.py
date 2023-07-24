while True:
    a=int(input())
    if a == -1:
        break
    p = [i for i in range(1,a) if a%i==0]
    if sum(p) == a:
        print(f'{a} = {" + ".join(map(str,p))}')
    else:
        print(f'{a} is NOT perfect.')