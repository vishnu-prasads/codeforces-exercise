s = list(map(str, input().strip()))
n = 0
for i in range(int(len(s)/2)):
    if s[i] == s[(-1-i)]:
        continue
    else: 
        n += 1
if (n == 0 and len(s)%2 == 1) or (n == 1):
    print("YES")
else:
    print("NO")