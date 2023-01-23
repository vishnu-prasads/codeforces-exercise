n = int(input())

for i in range(n):
    a, b = map(int,input().split())
    if  0 < a and 0 < b and a+b < 180:
        c = 180 - (a + b)
        if a == b == c:
            print("equilateral")
        elif(a==b or a==c or b==c):
            print("isosceles")
        else:
            print("scalene")
    else:
        exit()