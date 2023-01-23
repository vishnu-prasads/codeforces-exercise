def jump(a, b, k):
   if 1 <= a <= 1000000000 and 1 <= b <= 1000000000 and 1 <= k <= 1000000000:
            for j in range(k):
                if  k ==  1:
                    return (a)
                elif (k % 2 == 0):
                    return (a-b) * k // 2
                else:
                    return (a -b) * (k // 2) + a
   else:
       exit()


t = int(input())
if  1 <= t <= 1000:
    for i in range(t):
        a, b, k = map (int, input().split())
        result = jump(a, b, k)
        print (result)

else:
    exit()