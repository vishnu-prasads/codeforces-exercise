def team():
    count = 0
    n = int(input())
    if 1 <= n <= 1000:
        for i in range(n):
            a, b, c = map(int, input().split())
            if a == b == c == 1 or a == b == 1 or a == c == 1 or b == c == 1:
                count = count + 1

    else:
        exit()
    print(count)


team()


