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

#Input = 7 			output = 3
#Input = 1			output = 0
#Input = 2			output = 0
#Input = 3			output = 1
#Input = 2000000000	output = 999999999
#Input = 763243547	output = 763243547