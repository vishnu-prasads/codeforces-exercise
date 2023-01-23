n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
z = []
for i in range(n):
    if y[i] == x[i] + 10:
        continue
    else:
        z.append(x[i])
        z.append(y[i])

for j in range(len(z)):
    print(z[j], end=" ")
