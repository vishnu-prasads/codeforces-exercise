t = int(input())
if  1 <= t <= 1000:
    for i in range(t):
        d = 0
        c = 0
        a, b, k = map(int, input().split())
        if  a != b:
            if 1 <= a <= 1000000000 and 1 <= b <= 1000000000 and 1 <= k <= 1000000000:
                if k == 1:
                    print(a)
                elif k == 2:
                    print ( a - b)
                elif k == 3:
                    print ( a -  b + a)
                elif (k % 2) == 0:
                    d = a - b
                    c = k // 2
                    print(int(d * c))
                else:
                    d = a - b + a
                    c = k // 2
                    print(d * c + a)
            else:
                exit()
        else:
            if a == b and (k % 2) == 0:
                print ("0")
            else:
                print("1")
else:
    exit()