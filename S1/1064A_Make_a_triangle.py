a, b, c = map(int, input().split())
if a+b > c and a+c > b and b+c > a:
    print(0)
elif a>b and a>c :
    largest = a
    s1 = b
    s2 = c
    print(largest - s1 - s2 + 1)
elif b>a and b>c:
    largest = b
    s1 = a
    s2 = c
    print(largest - s1 - s2 + 1)
elif c>a and c>b:
    largest = c
    s1 = a
    s2 = b
    print(largest - s1 - s2 + 1)

