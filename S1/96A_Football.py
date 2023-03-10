n = list(map(int, input().strip()))
result = 0 
if len(n) > 7 and (n.count(0) >=7 or n.count(1) >= 7 ):
    for i in range(len(n)-1):
        if n[i] == n[i+1]:
            result += 1
        elif result <= 5:
            result = 0
if result >= 6:
    print("YES")
else:
    print("NO")

