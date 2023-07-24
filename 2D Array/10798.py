a = []

for _ in range(5):
    a.append(list(input()))
k = ''


for i in range(15):
    for j in range(5):
        try : 
            k += a[j][i]
        except:
            pass
print(k)