def elections(a,b,c):
    if 0 <= a <= 1000000000 and 0 <= b <= 1000000000 and 0 <= c <= 1000000000:
        if a == b == c:
            print(a+1,b+1,c+1)
        elif a == b and a > c:
            print (1,1,(a+1)-c)
        elif b == c and b > a:
            print ((b+1)-a,1,1)
        elif a == c and a > b:
            print(1,(a+1)-b,1)
        elif a > b and a > c:
            print (0,(a+1)-b,(a+1)-c)
        elif b > a and b > c:
            print((b+1)-a,0,(b+1)-c)
        elif c > a and c > b:
            print((c+1)-a,(c+1)-b,0)
        else:
            exit()
    else:
        exit()

t = int(input())
for i in range (t):
    if 1 <= t <= 100000:
        a,b,c = map (int, input().split())
        elections(a,b,c)
    else:
        exit()