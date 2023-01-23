a = list(map(int,input().split()))
o=[]
e=[]
for i in range(0,len(a)):
    if a[i] % 2 == 0:
        e.append(a[i])
    else:
        o.append(a[i])

n = e + o

for i in n:  
    print(i, end=" ")  
    