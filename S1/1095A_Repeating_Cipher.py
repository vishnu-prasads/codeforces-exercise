n = int(input())
s = list(map(str,input().strip()))
res = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
temp = []
for i in range(len(res)):
    while n > res[i]:
        temp.append(s[res[i]])
        break
print(*temp, sep="")
    

