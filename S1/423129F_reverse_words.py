r = []
txt = input()
x = txt.split(' ')


for i in range(0,len(x)):
    r.append(x[i] [::-1])

for i in r:  
    print(i, end=" ")  