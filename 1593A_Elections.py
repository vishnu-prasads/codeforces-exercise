def elections(a,b,c):
    if 0 <= a <= 1000000000 and 0 <= b <= 1000000000 and 0 <= c <= 1000000000:
        print(max(a, b + 1, c + 1) - a, max(a + 1, b, c + 1) - b, max(a + 1, b + 1, c) - c)
    else:
        exit()

t = int(input())
for i in range (t):
    if 1 <= t <= 100000:
        a,b,c = map (int, input().split())
        elections(a,b,c)
    else:
        exit()

