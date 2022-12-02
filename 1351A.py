t = int(input())
if t >0 and t <= 10**4:
    for i in range(t):
        a, b = map(int, input().split())
        if a >= -1000 and a <= 1000 and b >= -1000 and b <= 1000:
            print (a+b)
        else:
            exit()
else:
    exit()

