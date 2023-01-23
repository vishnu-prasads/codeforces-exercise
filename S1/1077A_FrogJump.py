t = int(input())
if  1 <= t <= 1000:
    for i in range(t):
        a, b, k = map(int, input().split())
        c = 1
        d = 0
        if  a != b:
            if 1 <= a <= 1000000000 and 1 <= b <= 1000000000 and 1 <= k <= 1000000000:
                for j in range(k):
                    if (c % 2) != 0:
                        d = d + a
                        c = c + 1
                    else:
                        d = d - b
                        c = c + 1
                print(d)
                d = 0
            else:
                exit()
        else:
            if a == b and (k % 2) == 0:
                print ("0")
            else:
                print("1")
else:
    exit()