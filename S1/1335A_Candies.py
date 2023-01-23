def candies(n):
    if 1 <= n <= 20000000000:
        if n == 1 or n == 2:
            print("0")
        elif n % 2 == 1:
            print(n//2)
        else:
            print((n//2)-1)
    else:
        exit()

t = int(input())
if 1 <= t <= 100000:
    for i in range(t):
        n = int (input())
        candies(n)
else:
    exit()

